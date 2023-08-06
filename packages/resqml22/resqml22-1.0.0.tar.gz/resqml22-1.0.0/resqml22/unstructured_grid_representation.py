from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.abstract_grid_representation import AbstractGridRepresentation
from resqml22.alternate_cell_index import AlternateCellIndex
from resqml22.unstructured_grid_geometry import UnstructuredGridGeometry

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class UnstructuredGridRepresentation(AbstractGridRepresentation):
    """Unstructured grid representation characterized by a cell count, and
    potentially nothing else.

    Both the oldest and newest simulation formats are based on this
    format.

    :ivar cell_count: Number of cells in the grid. Must be positive.
    :ivar original_cell_index:
    :ivar geometry:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    cell_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "CellCount",
            "type": "Element",
            "required": True,
            "min_inclusive": 1,
        }
    )
    original_cell_index: Optional[AlternateCellIndex] = field(
        default=None,
        metadata={
            "name": "OriginalCellIndex",
            "type": "Element",
        }
    )
    geometry: Optional[UnstructuredGridGeometry] = field(
        default=None,
        metadata={
            "name": "Geometry",
            "type": "Element",
        }
    )
