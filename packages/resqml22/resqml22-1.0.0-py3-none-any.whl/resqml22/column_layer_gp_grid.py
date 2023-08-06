from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from resqml22.ijk_gp_grid_patch import IjkGpGridPatch
from resqml22.kgaps import Kgaps
from resqml22.unstructured_column_layer_gp_grid_patch import UnstructuredColumnLayerGpGridPatch

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ColumnLayerGpGrid:
    """Used to construct a column layer grid patch based upon multiple
    unstructured column-layer and IJK grids that share a layering scheme.

    Multiple patches are supported.

    :ivar nk: Number of layers. Degenerate case (nk=0) is allowed for
        GPGrid.
    :ivar kgaps:
    :ivar ijk_gp_grid_patch:
    :ivar unstructured_column_layer_gp_grid_patch:
    """
    nk: Optional[int] = field(
        default=None,
        metadata={
            "name": "Nk",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
            "min_inclusive": 0,
        }
    )
    kgaps: Optional[Kgaps] = field(
        default=None,
        metadata={
            "name": "KGaps",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    ijk_gp_grid_patch: List[IjkGpGridPatch] = field(
        default_factory=list,
        metadata={
            "name": "IjkGpGridPatch",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    unstructured_column_layer_gp_grid_patch: List[UnstructuredColumnLayerGpGridPatch] = field(
        default_factory=list,
        metadata={
            "name": "UnstructuredColumnLayerGpGridPatch",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
