from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional, Union
from resqml22.abstract_representation import AbstractRepresentation
from resqml22.line_role import LineRole
from resqml22.polyline_set_patch import PolylineSetPatch

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class PolylineSetRepresentation(AbstractRepresentation):
    """A representation made up of a set of polylines or a set of polygonal
    chains (for more information, see PolylineRepresentation).

    For compactness, it is organized by line patch as a unique polyline set patch.
    If allPolylineClosed = True, all the polylines are connected between the first and the last point.
    Its geometry is a 1D array of points, corresponding to the concatenation of the points of all polyline points.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    line_role: Optional[Union[LineRole, str]] = field(
        default=None,
        metadata={
            "name": "LineRole",
            "type": "Element",
            "pattern": r".*:.*",
        }
    )
    line_patch: List[PolylineSetPatch] = field(
        default_factory=list,
        metadata={
            "name": "LinePatch",
            "type": "Element",
            "min_occurs": 1,
        }
    )
