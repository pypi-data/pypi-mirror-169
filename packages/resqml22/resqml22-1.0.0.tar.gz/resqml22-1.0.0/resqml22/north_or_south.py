from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class NorthOrSouth(Enum):
    """
    Specifies the north or south direction.

    :cvar NORTH: North of something.
    :cvar SOUTH: South of something.
    """
    NORTH = "north"
    SOUTH = "south"
