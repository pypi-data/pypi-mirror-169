from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from resqml22.abstract_plane_geometry import AbstractPlaneGeometry
from resqml22.three_point3d import ThreePoint3D

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class TiltedPlaneGeometry(AbstractPlaneGeometry):
    """
    Describes the geometry of a tilted (or potentially not tilted) plane from
    three points.
    """
    plane: List[ThreePoint3D] = field(
        default_factory=list,
        metadata={
            "name": "Plane",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "min_occurs": 1,
        }
    )
