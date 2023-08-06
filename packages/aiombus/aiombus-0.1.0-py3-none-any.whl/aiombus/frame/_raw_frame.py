"""Raw data MBus frame."""

import asyncio
import struct

from ._abstract_frame import AbstractMBusFrame
from ._util import calculate_checksum


class RawMBusFrame(AbstractMBusFrame):
    """Raw MBus frame as received via a serial connection."""

    def __init__(self):
        """Initialize MBus frame."""
        self.first_byte = b""
        self.head = b""
        self.data_head = b""
        self.data = b""
        self.foot = b""

    @property
    def body(self):
        """Return byte representation of the frame body."""
        return b"%b%b" % (self.data_head, self.data)

    def __bytes__(self):
        """Return byte representation of the frame."""
        return b"%b%b%b%b" % (self.first_byte, self.head, self.body, self.foot)

    @classmethod
    async def from_reader(cls, reader: asyncio.StreamReader):
        """Create raw MBus frame from stream reader."""
        # Read the first byte
        frame = cls()
        frame.first_byte = await reader.readexactly(1)

        if frame.first_byte == b"\xE5":
            return frame

        if frame.first_byte == b"\x10":
            frame.data_head = await reader.readexactly(2)

            frame.foot = _buf = await reader.readexactly(2)
            checksum, stop = struct.unpack("BB", _buf)

            assert calculate_checksum(frame.body) == checksum, "Checksum mismatch"
            assert stop == 0x16, "Invalid stop byte"

            return frame

        if frame.first_byte == b"\x68":
            frame.head = _buf = await reader.readexactly(3)

            length1, length2, start = struct.unpack("BBB", _buf)

            assert length1 == length2, "Length doesn't match"
            assert start == 0x68, "Unexpected start byte"

            frame.data_head = await reader.readexactly(3)

            data_len = length1 - 3
            if data_len > 0:
                frame.data = await reader.readexactly(data_len)

            frame.foot = _buf = await reader.readexactly(2)
            checksum, stop = struct.unpack("BB", _buf)

            assert calculate_checksum(frame.body) == checksum, "Checksum mismatch"
            assert stop == 0x16, "Invalid stop byte"

            return frame

        raise ValueError(f"Unknown first byte {frame.first_byte:b}")
