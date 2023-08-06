"""Variable length data block."""

from ._abstract_block import AbstractDataBlock
from ._bcd_block import decode_bcd, encode_bcd


class VariableLengthBlock(AbstractDataBlock):
    """Variable length data block."""

    DATA_FIELD_SPECIFIERS = [
        0x0D,
    ]

    def __init__(self, lvar=0, value=0):
        """Initialize variable length data block."""
        super().__init__()

        self._dif = 0x0D

        self.lvar = lvar
        self.value = 0

    @classmethod
    def from_stream(cls, dif, stream):
        """Construct VariableLengthBlock from stream."""
        block = super().from_stream(dif, stream)

        block.lvar = ord(stream.read(1))
        block.raw_value = stream.read(len(block))
        return block

    @property
    def raw_value(self):
        """Encode value to bytes."""
        if 0x00 <= self.lvar <= 0xBF:
            # ASCII
            return bytes(reversed(self.value))

        if 0xC0 <= self.lvar <= 0xCF:
            # Positive BCD number
            return encode_bcd(self.value, length=len(self))

        if 0xD0 <= self.lvar <= 0xDF:
            # Negative BCD number
            return encode_bcd(-self.value, length=len(self))

        if 0xE0 <= self.lvar <= 0xEF:
            # Binary number
            int.to_bytes(self.value, length=len(self), byteorder="little", signed=True)

        raise NotImplementedError(f"No encoder for LVAR {self.lvar:x}")

    @raw_value.setter
    def raw_value(self, raw_data):
        """Decode raw data to value."""
        if 0x00 <= self.lvar <= 0xBF:
            # ASCII
            self.value = bytes(reversed(raw_data))
        elif 0xC0 <= self.lvar <= 0xCF:
            # Positive BCD number
            self.value = decode_bcd(raw_data)
        elif 0xD0 <= self.lvar <= 0xDF:
            # Negative BCD number
            self.value = -decode_bcd(raw_data)
        elif 0xE0 <= self.lvar <= 0xEF:
            # Binary number with
            self.value = int.from_bytes(raw_data, byteorder="little", signed=True)
        else:
            raise NotImplementedError(f"No decoder for LVAR {self.lvar:x}")

    def __len__(self):
        """Length of data."""
        # We have a variable length block and have to calculate the length of the data
        if 0x00 <= self.lvar <= 0xBF:
            return self.lvar

        if 0xC0 <= self.lvar <= 0xCF:
            return self.lvar - 0xC0

        if 0xD0 <= self.lvar <= 0xDF:
            return self.lvar - 0xD0

        if 0xE0 <= self.lvar <= 0xEF:
            return self.lvar - 0xE0

        if 0xF0 <= self.lvar <= 0xFA:
            return self.lvar - 0xF0

        raise ValueError(f"LVAR field {self.lvar:x} not supported")

    @property
    def data(self):
        """Return byte representation of data."""
        return b"%c%b" % (self.lvar, self.raw_value)
