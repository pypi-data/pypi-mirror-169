from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from resqml22.abstract_integer_array import AbstractIntegerArray
from resqml22.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class IntervalGridCells:
    """Specifies the (Grid,Cell) intersection of each interval of the
    representation, if any.

    The information allows you to locate, on one or several grids, the
    intersection of volume (cells) and surface (faces) elements with a
    wellbore trajectory (existing or planned), streamline trajectories,
    or any polyline set.

    :ivar cell_count: The number of non-null entries in the grid indices
        array.
    :ivar grid_indices: The grid index for each interval of a
        representation. The grid index is specified by grid index array,
        to give the (Grid,Cell) index pair. Null values signify that the
        interval is not within a grid. BUSINESS RULE : Size of array =
        IntervalCount
    :ivar cell_indices: The cell index for each interval of a
        representation. The grid index is specified by grid index array,
        to give the (Grid,Cell) index pair. Null values signify that
        interval is not within a grid. BUSINESS RULE : Size of array =
        IntervalCount
    :ivar local_face_pair_per_cell_indices: For each cell, these are the
        entry and exit intersection faces of the trajectory in the cell.
        Use null for missing intersections, e.g., when a trajectory
        originates or terminates within a cell or when an interval is
        not within a grid. The local face-per-cell index is used because
        a global face index need not have been defined on the grid.
        BUSINESS RULE: Size of array = 2 * IntervalCount
    :ivar grid:
    """
    cell_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "CellCount",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
            "min_inclusive": 1,
        }
    )
    grid_indices: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "GridIndices",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    cell_indices: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "CellIndices",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    local_face_pair_per_cell_indices: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "LocalFacePairPerCellIndices",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    grid: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "Grid",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "min_occurs": 1,
        }
    )
