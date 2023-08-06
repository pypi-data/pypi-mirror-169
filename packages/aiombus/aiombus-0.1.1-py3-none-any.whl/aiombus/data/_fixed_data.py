"""Fixed MBus data structure."""


class FixedData:
    """Fixed data structure."""

    def __init__(self):
        """Initialize fixed data stricture."""
        raise NotImplementedError("Fixed data structure not implemented yet")

    def __bytes__(self):
        """Return byte representation of data structure."""
        return b""

    @classmethod
    def from_bytes(cls, data):
        """Parse data structure from stream."""
        raise NotImplementedError("Parsing of fixed data not implemented yet")
