from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class VolumetricThermalExpansionUom(Enum):
    """
    :cvar VALUE_1_DELTA_C: per delta Celsius
    :cvar VALUE_1_DELTA_F: per delta Fahrenheit
    :cvar VALUE_1_DELTA_K: per delta kelvin
    :cvar VALUE_1_DELTA_R: per delta Rankine
    :cvar VALUE_1_E_6_M3_M3_DELTA_C: (cubic metre per million cubic
        metre) per delta Celsius
    :cvar VALUE_1_E_6_M3_M3_DELTA_F: (cubic metre per million cubic
        metre) per delta Fahrenheit
    :cvar M3_M3_DELTA_K: cubic metre per cubic metre delta kelvin
    :cvar PPM_VOL_DELTA_C: (part per million [volume basis]) per delta
        Celsius
    :cvar PPM_VOL_DELTA_F: (part per million [volume basis)] per delta
        Fahrenheit
    """
    VALUE_1_DELTA_C = "1/deltaC"
    VALUE_1_DELTA_F = "1/deltaF"
    VALUE_1_DELTA_K = "1/deltaK"
    VALUE_1_DELTA_R = "1/deltaR"
    VALUE_1_E_6_M3_M3_DELTA_C = "1E-6 m3/(m3.deltaC)"
    VALUE_1_E_6_M3_M3_DELTA_F = "1E-6 m3/(m3.deltaF)"
    M3_M3_DELTA_K = "m3/(m3.deltaK)"
    PPM_VOL_DELTA_C = "ppm[vol]/deltaC"
    PPM_VOL_DELTA_F = "ppm[vol]/deltaF"
