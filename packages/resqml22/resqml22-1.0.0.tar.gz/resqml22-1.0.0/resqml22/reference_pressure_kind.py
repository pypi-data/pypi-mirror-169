from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class ReferencePressureKind(Enum):
    """
    ReferencePressureKind.

    :cvar ABSOLUTE: absolute
    :cvar AMBIENT: ambient
    :cvar LEGAL:
    """
    ABSOLUTE = "absolute"
    AMBIENT = "ambient"
    LEGAL = "legal"
