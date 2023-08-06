"""Speciality block types."""

from ._abstract_block import AbstractDataBlock


class NoDataBlock(AbstractDataBlock):
    """No data block."""

    DATA_FIELD_SPECIFIERS = [
        0x00,
    ]

    @property
    def data(self):
        """Return byte representation of data."""
        return b""


class SelectionForReadoutBlock(AbstractDataBlock):
    """Selection for readout block."""

    DATA_FIELD_SPECIFIERS = [
        0x08,
    ]

    @property
    def data(self):
        """Return byte representation of data."""
        return b""
