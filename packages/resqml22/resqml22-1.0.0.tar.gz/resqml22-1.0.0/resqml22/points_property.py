from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from resqml22.abstract_point3d_array import AbstractPoint3DArray
from resqml22.abstract_property import AbstractProperty

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class PointsProperty(AbstractProperty):
    """
    Represents the geometric information that should *not* be used as
    representation geometry, but should be used in another context where the
    location or geometrical vectorial distances are needed.

    :ivar points_for_patch: Geometric points (or vectors) to be attached
        to the specified indexable elements.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    points_for_patch: List[AbstractPoint3DArray] = field(
        default_factory=list,
        metadata={
            "name": "PointsForPatch",
            "type": "Element",
            "min_occurs": 1,
        }
    )
