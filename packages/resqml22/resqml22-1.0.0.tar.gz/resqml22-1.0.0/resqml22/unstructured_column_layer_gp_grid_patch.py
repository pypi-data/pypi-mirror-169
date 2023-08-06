from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.truncation_cell_patch import TruncationCellPatch
from resqml22.unstructured_column_layer_grid_geometry import UnstructuredColumnLayerGridGeometry

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class UnstructuredColumnLayerGpGridPatch:
    """Used to specify unstructured column-layer grid patch(es) within a
    general purpose grid.

    Multiple patches are supported.

    :ivar unstructured_column_count: Number of unstructured columns.
        Degenerate case (count=0) is allowed for GPGrid.
    :ivar geometry:
    :ivar truncation_cell_patch:
    """
    unstructured_column_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "UnstructuredColumnCount",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
            "min_inclusive": 0,
        }
    )
    geometry: Optional[UnstructuredColumnLayerGridGeometry] = field(
        default=None,
        metadata={
            "name": "Geometry",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    truncation_cell_patch: Optional[TruncationCellPatch] = field(
        default=None,
        metadata={
            "name": "TruncationCellPatch",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
