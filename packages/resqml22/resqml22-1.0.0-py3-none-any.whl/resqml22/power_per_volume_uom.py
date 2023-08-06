from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class PowerPerVolumeUom(Enum):
    """
    :cvar BTU_IT_H_FT3: BTU per hour cubic foot
    :cvar BTU_IT_S_FT3: (BTU per second) per cubic foot
    :cvar CAL_TH_H_CM3: calorie per hour cubic centimetre
    :cvar CAL_TH_S_CM3: calorie per second cubic centimetre
    :cvar HP_FT3: horsepower per cubic foot
    :cvar K_W_M3: kilowatt per cubic metre
    :cvar U_W_M3: microwatt per cubic metre
    :cvar W_M3: watt per cubic metre
    """
    BTU_IT_H_FT3 = "Btu[IT]/(h.ft3)"
    BTU_IT_S_FT3 = "Btu[IT]/(s.ft3)"
    CAL_TH_H_CM3 = "cal[th]/(h.cm3)"
    CAL_TH_S_CM3 = "cal[th]/(s.cm3)"
    HP_FT3 = "hp/ft3"
    K_W_M3 = "kW/m3"
    U_W_M3 = "uW/m3"
    W_M3 = "W/m3"
