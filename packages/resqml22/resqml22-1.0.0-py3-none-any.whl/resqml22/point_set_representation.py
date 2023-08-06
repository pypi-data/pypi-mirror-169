from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from resqml22.abstract_representation import AbstractRepresentation
from resqml22.point_geometry import PointGeometry

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class PointSetRepresentation(AbstractRepresentation):
    """A representation that consists of one or more node patches.

    Each node patch is an array of XYZ coordinates for the 3D points.
    There is no implied linkage between the multiple patches.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    node_patch_geometry: List[PointGeometry] = field(
        default_factory=list,
        metadata={
            "name": "NodePatchGeometry",
            "type": "Element",
            "min_occurs": 1,
        }
    )
