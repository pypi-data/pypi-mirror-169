"""Common methods and classes."""

import enum


class Byte(enum.Enum):
    """Byte enum type."""

    def __init__(self, byte, mask, info=None):
        """Create Byte enumeration."""
        self._value_ = byte
        self.mask = mask

        if info is not None:
            self.info = info

    @classmethod
    def _missing_(cls, value):
        for item in cls:
            if (value & item.mask) == item.value:
                return item

        raise KeyError(f"No such item {value:02X}")
