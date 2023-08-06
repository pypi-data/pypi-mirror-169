from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from resqml22.abstract_plane_geometry import AbstractPlaneGeometry
from resqml22.abstract_surface_representation import AbstractSurfaceRepresentation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class PlaneSetRepresentation(AbstractSurfaceRepresentation):
    """Defines a plane representation, which can be made up of multiple
    patches.

    Commonly represented features are fluid contacts or frontiers.
    Common geometries of this representation are titled or horizontal
    planes. BUSINESS RULE: If the plane representation is made up of
    multiple patches, then you must specify the outer rings for each
    plane patch.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    planes: List[AbstractPlaneGeometry] = field(
        default_factory=list,
        metadata={
            "name": "Planes",
            "type": "Element",
            "min_occurs": 1,
        }
    )
