from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


class Shape3D(Enum):
    """
    Enumeration characterizing the 3D shape of a geological unit.
    """
    SHEET = "sheet"
    DYKE = "dyke"
    DOME = "dome"
    MUSHROOM = "mushroom"
    CHANNEL = "channel"
    DELTA = "delta"
    DUNE = "dune"
    FAN = "fan"
    REEF = "reef"
    WEDGE = "wedge"
