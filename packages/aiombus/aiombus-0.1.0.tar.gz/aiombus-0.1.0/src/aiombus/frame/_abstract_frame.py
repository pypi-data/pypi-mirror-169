"""Abstract MBus frame."""
import binascii


class AbstractMBusFrame:
    """Abstract MBus frame."""

    def __repr__(self):
        """Return a readable byte representation of the MBus frame."""
        _bytes = binascii.hexlify(bytes(self), sep=" ")
        return f"<{self.__class__.__name__} {_bytes}>"

    def __eq__(self, other: object) -> bool:
        """Test for bytewise equality."""
        return bytes(self) == bytes(other)
