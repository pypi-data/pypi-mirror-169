from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.abstract_truncated_column_layer_grid_representation import AbstractTruncatedColumnLayerGridRepresentation
from resqml22.unstructured_column_layer_grid_geometry import UnstructuredColumnLayerGridGeometry

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class TruncatedUnstructuredColumnLayerGridRepresentation(AbstractTruncatedColumnLayerGridRepresentation):
    """Grid class with an underlying unstructured column-layer topology,
    together with a 1D split-cell list.

    The truncated cells have more than the usual number of faces within
    each column. The split cells are arbitrary polyhedra, identical to
    those of an unstructured cell grid.

    :ivar column_count: Number of unstructured columns in the grid. Must
        be positive.
    :ivar geometry:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    column_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "ColumnCount",
            "type": "Element",
            "required": True,
            "min_inclusive": 1,
        }
    )
    geometry: Optional[UnstructuredColumnLayerGridGeometry] = field(
        default=None,
        metadata={
            "name": "Geometry",
            "type": "Element",
            "required": True,
        }
    )
