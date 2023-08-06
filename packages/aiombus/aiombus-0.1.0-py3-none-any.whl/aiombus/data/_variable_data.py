"""Variable MBus data."""

import io
from fcntl import F_UNLCK

from .block import BLOCK_TYPES, AbstractBlock, Function, SpecialFunctionsBlock


class VariableData:
    """Variable MBus data."""

    def __init__(self):
        """Initialize variable data object."""
        self._blocks = []

        self.header = b""
        self.manufacturer_specific = b""

    def __bytes__(self):
        """Return byte representation."""
        _blocks = b"".join([bytes(block) for block in self._blocks])

        return b"%b%b%b" % (
            self.header,
            _blocks,
            self.manufacturer_specific,
        )

    def append_block(self, block: AbstractBlock):
        """Add block."""
        self._blocks.append(block)

    def _parse_header(self, header: bytes):
        """Parse 12 byte header."""
        # TODO: parse header
        self.header = header

    @property
    def more_frames_to_follow(self):
        """Check if more frames are to follow."""
        return (
            isinstance(self._blocks[-1], SpecialFunctionsBlock)
            and self._blocks[-1].function == Function.NEXT_TELEGRAM
        )

    @classmethod
    def from_bytes(cls, data: bytes):
        """Parse data object from byte stream."""
        data_obj = cls()

        # Convert data into BytesIO object to consume it piece by piece
        stream = io.BytesIO(data)

        # The first 12 bytes contain a fixed data header
        _header = stream.read(12)
        data_obj._parse_header(_header)

        # We begin to parse the data blocks
        while True:
            # Read next data block
            _dif = ord(stream.read(1))
            block_cls = BLOCK_TYPES[_dif & 0x0F]

            block = block_cls.from_stream(_dif, stream)
            data_obj.append_block(block)

            if block_cls == SpecialFunctionsBlock and (
                block.function == Function.END_OF_USER_DATA
                or block.function == Function.NEXT_TELEGRAM
            ):
                break

        data_obj.manufacturer_specific = stream.read()

        return data_obj
