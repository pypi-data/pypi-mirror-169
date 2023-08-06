"""Data blocks."""

from ._abstract_block import AbstractBlock, AbstractDataBlock
from ._bcd_block import BCDBlock
from ._blocks import NoDataBlock, SelectionForReadoutBlock
from ._int_block import IntegerBlock
from ._lvar_block import VariableLengthBlock
from ._real_block import RealBlock
from ._special_functions_block import Function, SpecialFunctionsBlock

_CLS = [
    BCDBlock,
    NoDataBlock,
    SelectionForReadoutBlock,
    IntegerBlock,
    VariableLengthBlock,
    RealBlock,
    SpecialFunctionsBlock,
]

BLOCK_TYPES = {_s: cls for cls in _CLS for _s in cls.DATA_FIELD_SPECIFIERS}

__all__ = [
    "AbstractBlock",
    "AbstractDataBlock",
    "BCDBlock",
    "NoDataBlock",
    "SelectionForReadoutBlock",
    "IntegerBlock",
    "VariableLengthBlock",
    "RealBlock",
    "SpecialFunctionsBlock",
    "Function",
]
