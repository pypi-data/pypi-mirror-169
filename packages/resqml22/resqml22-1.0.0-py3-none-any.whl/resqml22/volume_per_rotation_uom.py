from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class VolumePerRotationUom(Enum):
    """
    :cvar FT3_RAD: cubic foot per radian
    :cvar M3_RAD: cubic metre per radian
    :cvar M3_REV: cubic metre per revolution
    """
    FT3_RAD = "ft3/rad"
    M3_RAD = "m3/rad"
    M3_REV = "m3/rev"
