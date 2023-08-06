from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.abstract_column_layer_grid_geometry import AbstractColumnLayerGridGeometry
from resqml22.ij_gaps import IjGaps

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class IjkGridGeometry(AbstractColumnLayerGridGeometry):
    """Explicit geometry definition for the cells of the IJK grid.

    Grid options are also defined through this data-object.

    :ivar grid_is_righthanded: Indicates that the IJK grid is right
        handed, as determined by the triple product of tangent vectors
        in the I, J, and K directions.
    :ivar ij_gaps:
    """
    grid_is_righthanded: Optional[bool] = field(
        default=None,
        metadata={
            "name": "GridIsRighthanded",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    ij_gaps: Optional[IjGaps] = field(
        default=None,
        metadata={
            "name": "IjGaps",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
