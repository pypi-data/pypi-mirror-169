"""Abstract definition of MBus frame blocks."""

from abc import ABC, abstractmethod


def information_block(first_byte: int, extension: list[int]) -> bytes:
    """
    Format the data or value information block.

    :param fb: First byte, i.e. DIF or VIF
    :param ext: Extension bytes, i.e. DIFE or VIFE
    """
    if first_byte is None:
        return b""

    if len(extension) == 0:
        # If no extension is present, erase the extension bit
        return b"%c" % (first_byte & 0x7F)

    *_es, _e = extension
    return b"%c%b%c" % (first_byte | 0x80, bytes([_b | 0x80 for _b in _es]), _e & 0x7F)


class AbstractBlock(ABC):
    """Block in variable data MBus frame."""

    DATA_FIELD_SPECIFIERS = []

    def __init__(self):
        """Initialize block."""
        self._dif = 0x00
        self._dife = []

        # Initialize vif and vife variables
        self._vif = None
        self._vife = []

    @property
    def dif(self):
        """Return DIF."""
        return self._dif

    @property
    def dife(self):
        """Return DIFE."""
        return self._dife

    @property
    def vif(self):
        """Return VIF."""
        return self._vif

    @property
    def vife(self):
        """Return VIFE."""
        return self._vife

    @property
    def drh(self):
        """Return the data record header."""
        return b"%b%b" % (
            information_block(self.dif, self.dife),
            information_block(self.vif, self.vife),
        )

    @classmethod
    @abstractmethod
    def from_stream(cls, dif, stream):
        """Construct block from stream."""

    @abstractmethod
    def __bytes__(self):
        """Return byte representation of block."""


class AbstractDataBlock(AbstractBlock):
    """Block representing a generic data value and unit."""

    def __init__(self):
        """Inititalize block."""
        super().__init__()

        self._value = 0

    @property
    def value(self):
        """Return value of data block."""
        return self._value

    @value.setter
    def value(self, new_value):
        """Set value of data block."""
        self._value = new_value

    @classmethod
    def from_stream(cls, dif, stream):
        """Parse data block from stream."""
        block = cls()
        block._dif = dif

        # Read data information field extensions
        _e = dif & 0x80
        while _e:
            dife = ord(stream.read(1))
            block._dife.append(dife)

            _e = dife & 0x80

        # Read value information field
        block._vif = vif = ord(stream.read(1))

        # Read value information field extensions
        _e = vif & 0x80
        while _e:
            vife = ord(stream.read(1))
            block._vife.append(vife)

            _e = vife & 0x80

        return block

    @property
    @abstractmethod
    def data(self) -> bytes:
        """Return byte representation of data."""

    def __bytes__(self) -> bytes:
        """Return byte representation of data block."""
        return b"%b%b" % (self.drh, self.data)
