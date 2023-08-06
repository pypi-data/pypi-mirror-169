from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from resqml22.abstract_surface_representation import AbstractSurfaceRepresentation
from resqml22.triangle_patch import TrianglePatch

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class TriangulatedSetRepresentation(AbstractSurfaceRepresentation):
    """A representation based on set of triangulated mesh patches, which gets
    its geometry from a 1D array of points.

    BUSINESS RULE: The orientation of all the triangles of this
    representation must be consistent.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    triangle_patch: List[TrianglePatch] = field(
        default_factory=list,
        metadata={
            "name": "TrianglePatch",
            "type": "Element",
            "min_occurs": 1,
        }
    )
