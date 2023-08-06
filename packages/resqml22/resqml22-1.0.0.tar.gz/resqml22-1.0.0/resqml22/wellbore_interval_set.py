from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from resqml22.abstract_representation import AbstractRepresentation
from resqml22.marker_boundary import MarkerBoundary
from resqml22.marker_interval import MarkerInterval

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class WellboreIntervalSet(AbstractRepresentation):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    interval_boundaries: List[MarkerBoundary] = field(
        default_factory=list,
        metadata={
            "name": "IntervalBoundaries",
            "type": "Element",
        }
    )
    marker_interval: List[MarkerInterval] = field(
        default_factory=list,
        metadata={
            "name": "MarkerInterval",
            "type": "Element",
            "min_occurs": 1,
        }
    )
