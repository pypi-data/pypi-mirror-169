"""MBus frame class."""

import enum
import struct

from .._common import Byte
from ..data import VariableData
from ._abstract_frame import AbstractMBusFrame
from ._raw_frame import RawMBusFrame


class FrameType(enum.Enum):
    """Valid frame types."""

    ACKNOWLEDGE = 1
    SHORT = 2
    LONG = 3


class Control(Byte):  # pylint: disable=too-few-public-methods
    """Valid control byte values."""

    SND_NKE = 0x40, 0b11011111
    SND_UD = 0x53, 0b11011111
    REQ_UD2 = 0x5B, 0b11011111
    REQ_UD1 = 0x5A, 0b11011111
    RSP_UD = 0x08, 0b11001111


class ControlInformation(Byte):  # pylint: disable=too-few-public-methods
    """Valid control information byte values."""

    DATA_SEND = 0x51, 0b11111011
    SLAVE_SELECT = 0x52, 0b11111011

    APPLICATION_RESET = 0x50, 0xFF
    SYNC_ACTION = 0x54, 0xFF

    GENERAL_APPLICATION_ERROR = 0x70, 0xFF
    ALARM_STATUS = 0x71, 0xFF

    VARIABLE_DATA = 0x72, 0b11111011
    FIXED_DATA = 0x73, 0b11111011


FCB_BIT = 5

ACD_BIT = 5
DFC_BIT = 4


class Frame(AbstractMBusFrame):
    """MBus frame."""

    def __init__(
        self,
        frame_type: FrameType,
        control: Control = None,
        address: int = 0xFF,
        control_information: ControlInformation = None,
        **kwargs,
    ):
        """Initialize MBus frame."""
        self._type = frame_type

        self._c = control.value if control is not None else None
        self._a = address
        self._ci = control_information

        if self._c is not None:
            if Control(self._c) in [
                Control.SND_NKE,
                Control.SND_UD,
                Control.REQ_UD2,
                Control.REQ_UD1,
            ]:
                self._c |= kwargs.get("fcb", False) << FCB_BIT

            if Control(self._c) in [
                Control.RSP_UD,
            ]:
                self._c |= kwargs.get("acd", False) << ACD_BIT
                self._c |= kwargs.get("dfc", False) << DFC_BIT

        self.data = b""

    def flip_fcb(self):
        """Flip the frame count bit."""
        self._c ^= 1 << FCB_BIT

    def __bytes__(self):  # pylint: disable=inconsistent-return-statements
        """Return byte representation of MBus frame."""
        if self._type == FrameType.ACKNOWLEDGE:
            return b"\xE5"

        if self._type == FrameType.SHORT:
            return b"\x10%b%c\x16" % (self.body, self.checksum)

        if self._type == FrameType.LONG:
            return b"\x68%c%c\x68%b%c\x16" % (
                len(self),
                len(self),
                self.body,
                self.checksum,
            )

    @property
    def body(self):
        """Return data body of MBus frame."""
        if self._type == FrameType.SHORT:
            return b"%c%c" % (self._c, self._a)

        if self._type == FrameType.LONG:
            return b"%c%c%c%b" % (
                self._c,
                self._a,
                self._ci,
                self.data,
            )

        return b""

    def __len__(self):
        """Return length of MBus frame data as indicated in the header."""
        return len(self.body)

    @property
    def checksum(self):
        """Return checksum."""
        return sum([int(byte) for byte in self.body]) % 256

    @classmethod
    def from_raw_frame(cls, raw_frame: RawMBusFrame):
        """Create MBus frame from byte reader."""
        if raw_frame.first_byte == b"\xE5":
            return cls(frame_type=FrameType.ACKNOWLEDGE)

        if raw_frame.first_byte == b"\x10":
            frame = cls(frame_type=FrameType.SHORT)
            frame._c, frame._a = struct.unpack("BB", raw_frame.body)

            return frame

        if raw_frame.first_byte == b"\x68":
            frame = cls(frame_type=FrameType.LONG)
            frame._c, frame._a, frame._ci = struct.unpack("BBB", raw_frame.body[:3])

            if len(raw_frame.body) > 3:
                _ci = ControlInformation(frame._ci)
                if _ci == ControlInformation.VARIABLE_DATA:
                    data_cls = VariableData
                else:
                    raise NotImplementedError

                frame.data = data_cls.from_bytes(raw_frame.body[3:])

            return frame

        raise ValueError(f"Unknown first byte {raw_frame.first_byte:b}")
