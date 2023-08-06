from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.abstract_geometry import AbstractGeometry
from resqml22.point3d import Point3D

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class SinglePointGeometry(AbstractGeometry):
    """
    The geometry of a single point defined by its location in the local CRS.
    """
    point3d: Optional[Point3D] = field(
        default=None,
        metadata={
            "name": "Point3d",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
