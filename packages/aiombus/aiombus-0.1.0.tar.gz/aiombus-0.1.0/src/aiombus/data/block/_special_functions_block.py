"""Special function block."""
from enum import Enum

from ._abstract_block import AbstractBlock


class Function(Enum):
    """Special function."""

    END_OF_USER_DATA = 0x0F
    NEXT_TELEGRAM = 0x1F
    IDLE_FILLER = 0x2F
    GLOBAL_READOUT_REQUEST = 0x7F


class SpecialFunctionsBlock(AbstractBlock):
    """Special functions block."""

    DATA_FIELD_SPECIFIERS = [
        0x0F,
    ]

    def __init__(self, function: Function = Function.END_OF_USER_DATA):
        """Initialize special functions block."""
        super().__init__()

        self.function = function

    @property
    def dif(self):
        """Return DIF."""
        return self.function.value

    @classmethod
    def from_stream(cls, dif, stream):
        """Construct SpecialFunctionsBlock from stream."""
        block = cls()
        block.function = Function(dif)

        return block

    def __bytes__(self):
        """Return byte representation of block."""
        return b"%c" % self.dif
