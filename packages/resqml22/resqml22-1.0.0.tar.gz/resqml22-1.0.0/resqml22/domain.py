from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


class Domain(Enum):
    """
    An enumeration that specifies in which domain the interpretation of an
    AbstractFeature has been performed: depth, time, or mixed (= depth + time).

    :cvar DEPTH: Position defined by measurements in the depth domain.
    :cvar TIME: Position based on geophysical measurements in two-way
        time (TWT).
    :cvar MIXED: depth + time
    """
    DEPTH = "depth"
    TIME = "time"
    MIXED = "mixed"
