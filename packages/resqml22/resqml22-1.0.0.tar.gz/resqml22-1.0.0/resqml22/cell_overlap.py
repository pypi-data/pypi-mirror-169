from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.abstract_integer_array import AbstractIntegerArray
from resqml22.overlap_volume import OverlapVolume

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class CellOverlap:
    """Optional cell volume overlap information between the current grid (the
    child) and the parent grid.

    Use this data-object when the child grid has an explicitly defined
    geometry, and these relationships cannot be inferred from the regrid
    descriptions.

    :ivar count: Number of parent-child cell overlaps. Must be positive.
    :ivar parent_child_cell_pairs: (Parent cell index, child cell index)
        pair for each overlap. BUSINESS RULE: Length of array must equal
        2 x overlapCount.
    :ivar overlap_volume:
    """
    count: Optional[int] = field(
        default=None,
        metadata={
            "name": "Count",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
            "min_inclusive": 1,
        }
    )
    parent_child_cell_pairs: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "ParentChildCellPairs",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    overlap_volume: Optional[OverlapVolume] = field(
        default=None,
        metadata={
            "name": "OverlapVolume",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
