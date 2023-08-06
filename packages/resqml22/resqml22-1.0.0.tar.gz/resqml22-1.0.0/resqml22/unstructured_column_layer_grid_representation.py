from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.abstract_column_layer_grid_representation import AbstractColumnLayerGridRepresentation
from resqml22.unstructured_column_layer_grid_geometry import UnstructuredColumnLayerGridGeometry

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class UnstructuredColumnLayerGridRepresentation(AbstractColumnLayerGridRepresentation):
    """Grid whose topology is characterized by an unstructured column index and
    a layer index, K.

    Cell geometry is characterized by nodes on coordinate lines, where
    each column of the model may have an arbitrary number of sides.

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
        }
    )
