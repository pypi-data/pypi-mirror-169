"""Data block representing an integer."""

from ._abstract_block import AbstractDataBlock


class IntegerBlock(AbstractDataBlock):
    """Integer data block."""

    _DEF = [
        (0x01, 1),
        (0x02, 2),
        (0x03, 3),
        (0x04, 4),
        (0x06, 6),
        (0x07, 8),
    ]

    _DIF = {l: b for (b, l) in _DEF}
    _LENGTH = {b: l for (b, l) in _DEF}

    DATA_FIELD_SPECIFIERS = [b for b, _ in _DEF]

    def __init__(self, value=0, length=1):
        """Initialize integer data block."""
        super().__init__()

        self.value = value
        self.length = length

    def __len__(self):
        """Return length of data field."""
        return self.length

    @property
    def dif(self):
        """Return DIF."""
        return (self._dif & 0xF0) | self._DIF[len(self)]

    @property
    def data(self):
        """Get byte representation of value."""
        return int.to_bytes(
            self.value, length=len(self), byteorder="little", signed=True
        )

    @classmethod
    def from_stream(cls, dif, stream):
        """Construct IntegerBlock from stream."""
        # Create instance and parse DRH
        block = super().from_stream(dif, stream)

        block.length = cls._LENGTH[dif & 0x0F]

        data = stream.read(len(block))
        block.value = int.from_bytes(data, byteorder="little", signed=True)

        return block
