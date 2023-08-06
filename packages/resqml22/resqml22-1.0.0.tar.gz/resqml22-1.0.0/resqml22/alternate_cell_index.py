from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from resqml22.abstract_integer_array import AbstractIntegerArray
from resqml22.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class AlternateCellIndex:
    """Allows definition of an alternate cell indexing for a representation.

    If defined, this alternate cell indexing is the only one to rely on
    when referencing the representation cells. The alternate cell
    indices must come from existing grid representations. Because this
    alternate indexing requires a lot of extra work for software readers
    to process, use only when no other solution is acceptable.

    :ivar cell_index: Defines each alternate cell index for each
        representation cell. BUSINESS RULE :CellIndex.Count =
        GridIndex.Count = Representation.Cell.Count
    :ivar grid_index: Defines which grid each alternate cell index comes
        from. The grids are defined by means of an index of the
        OriginalGrids set. BUSINESS RULE : GridIndex.Count =
        CellIndex.Count = Representation.Cell.Count
    :ivar original_grids:
    """
    cell_index: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "CellIndex",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    grid_index: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "GridIndex",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    original_grids: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "OriginalGrids",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "min_occurs": 1,
        }
    )
