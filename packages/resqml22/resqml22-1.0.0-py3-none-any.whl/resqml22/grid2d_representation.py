from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.abstract_surface_representation import AbstractSurfaceRepresentation
from resqml22.point_geometry import PointGeometry

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class Grid2DRepresentation(AbstractSurfaceRepresentation):
    """Representation based on a 2D grid.

    For definitions of slowest and fastest axes of the array, see
    Grid2dPatch.
    """
    class Meta:
        name = "Grid2dRepresentation"
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    fastest_axis_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "FastestAxisCount",
            "type": "Element",
            "required": True,
            "min_inclusive": 1,
        }
    )
    slowest_axis_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "SlowestAxisCount",
            "type": "Element",
            "required": True,
            "min_inclusive": 1,
        }
    )
    geometry: Optional[PointGeometry] = field(
        default=None,
        metadata={
            "name": "Geometry",
            "type": "Element",
            "required": True,
        }
    )
