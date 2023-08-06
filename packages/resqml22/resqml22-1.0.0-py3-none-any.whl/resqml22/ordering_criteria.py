from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


class OrderingCriteria(Enum):
    """
    Enumeration used to specify the order of an abstract stratigraphic
    organization or a structural organization interpretation.

    :cvar AGE: From youngest to oldest period (increasing age).
    :cvar APPARENT_DEPTH: From surface to subsurface.
    """
    AGE = "age"
    APPARENT_DEPTH = "apparent depth"
