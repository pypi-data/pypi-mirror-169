from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class ThermalInsulanceUom(Enum):
    """
    :cvar DELTA_C_M2_H_KCAL_TH: delta Celsius square metre hour per
        thousand calory
    :cvar DELTA_F_FT2_H_BTU_IT: delta Fahrenheit square foot hour per
        BTU
    :cvar DELTA_K_M2_K_W: delta kelvin square metre per kilowatt
    :cvar DELTA_K_M2_W: delta kelvin square metre per watt
    """
    DELTA_C_M2_H_KCAL_TH = "deltaC.m2.h/kcal[th]"
    DELTA_F_FT2_H_BTU_IT = "deltaF.ft2.h/Btu[IT]"
    DELTA_K_M2_K_W = "deltaK.m2/kW"
    DELTA_K_M2_W = "deltaK.m2/W"
