from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class TemperatureIntervalPerLengthUom(Enum):
    """
    :cvar VALUE_0_01_DELTA_F_FT: delta Fahrenheit per hundred foot
    :cvar DELTA_C_FT: delta Celsius per foot
    :cvar DELTA_C_HM: delta Celsius per hectometre
    :cvar DELTA_C_KM: delta Celsius per kilometre
    :cvar DELTA_C_M: delta Celsius per metre
    :cvar DELTA_F_FT: delta Fahrenheit per foot
    :cvar DELTA_F_M: delta Fahrenheit per metre
    :cvar DELTA_K_KM: delta kelvin per kilometre
    :cvar DELTA_K_M: delta kelvin per metre
    """
    VALUE_0_01_DELTA_F_FT = "0.01 deltaF/ft"
    DELTA_C_FT = "deltaC/ft"
    DELTA_C_HM = "deltaC/hm"
    DELTA_C_KM = "deltaC/km"
    DELTA_C_M = "deltaC/m"
    DELTA_F_FT = "deltaF/ft"
    DELTA_F_M = "deltaF/m"
    DELTA_K_KM = "deltaK/km"
    DELTA_K_M = "deltaK/m"
