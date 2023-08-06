"""Data block representing an floating point value."""

import struct

from ._abstract_block import AbstractDataBlock


class RealBlock(AbstractDataBlock):
    """Floating point data block."""

    DATA_FIELD_SPECIFIERS = [
        0x05,
    ]

    def __init__(self, value=0):
        """Initialize floating point data block."""
        super().__init__()

        self.value = value

    def __len__(self):
        """Return length of data field."""
        return 4

    @property
    def dif(self):
        """Return DIF."""
        return (self._dif & 0xF0) | 0x05

    @property
    def data(self):
        """Get byte representation of value."""
        return struct.pack("<f", self.value)

    @classmethod
    def from_stream(cls, dif, stream):
        """Construct block from stream."""
        # Create instance and parse DRH
        block = super().from_stream(dif, stream)

        data = stream.read(len(block))
        (block.value,) = struct.unpack("<f", data)

        return block
