from __future__ import annotations
from dataclasses import dataclass
from resqml22.marker_boundary import MarkerBoundary

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class FluidIntervalBoundary(MarkerBoundary):
    """
    This represents a boundary between two intervals where at least one side of
    the boundary is a fluid.
    """
