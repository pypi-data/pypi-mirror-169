"""BCD data block."""

from ._abstract_block import AbstractDataBlock


def encode_bcd(value, length):
    """
    Encode unsigned integer value as BCD.

    :param value: Integer value to encode
    :param length: Byte length of output
    """
    _div = 100**length
    _bs = []

    assert _div > value > 0, "Value out of bounds"

    while _div > 1:
        _div = _div // 100

        _a, _b = divmod(value // _div, 10)

        _bs.append((_a << 4) | _b)
        value %= _div

    return bytes(_bs)


def decode_bcd(byte_string):
    """
    Decode binary coded decimal.

    :param byte_string: Byte string to decode
    """
    value = 0
    for byte in list(byte_string):
        value *= 100
        value += ((byte & 0xF0) >> 4) * 10 + (byte & 0x0F)

    return value


class BCDBlock(AbstractDataBlock):
    """BCD data block."""

    _DEF = [
        (0x09, 1),
        (0x0A, 2),
        (0x0B, 3),
        (0x0C, 4),
        (0x0E, 6),
    ]

    _DIF = {l: b for (b, l) in _DEF}
    _LENGTH = {b: l for (b, l) in _DEF}

    DATA_FIELD_SPECIFIERS = [b for b, _ in _DEF]

    def __init__(self, value=0, length=1):
        """Create BCD data block."""
        super().__init__()

        self.value = value
        self.length = length

    def __len__(self):
        """Length of data."""
        return self.length

    @property
    def dif(self):
        """Return DIF."""
        return (self._dif & 0xF0) | self._DIF[len(self)]

    @classmethod
    def from_stream(cls, dif, stream):
        """Create BCDBlock from stream."""
        block = super().from_stream(dif, stream)  # type: 'BCDBlock'

        block.length = cls._LENGTH[dif & 0x0F]
        block.value = decode_bcd(stream.read(len(block)))

        return block

    @property
    def data(self):
        """Encode value."""
        return encode_bcd(self.value, len(self))
