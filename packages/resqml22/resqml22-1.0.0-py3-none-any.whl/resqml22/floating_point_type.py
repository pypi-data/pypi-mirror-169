from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class FloatingPointType(Enum):
    ARRAY_OF_FLOAT32_LE = "arrayOfFloat32LE"
    ARRAY_OF_DOUBLE64_LE = "arrayOfDouble64LE"
    ARRAY_OF_FLOAT32_BE = "arrayOfFloat32BE"
    ARRAY_OF_DOUBLE64_BE = "arrayOfDouble64BE"
