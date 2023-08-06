from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class PressurePerTimeUom(Enum):
    """
    :cvar ATM_H: standard atmosphere per hour
    :cvar BAR_H: bar per hour
    :cvar K_PA_H: kilopascal per hour
    :cvar K_PA_MIN: kilopascal per min
    :cvar MPA_H: megapascal per hour
    :cvar PA_H: pascal per hour
    :cvar PA_S: pascal per second
    :cvar PSI_H: psi per hour
    :cvar PSI_MIN: psi per minute
    """
    ATM_H = "atm/h"
    BAR_H = "bar/h"
    K_PA_H = "kPa/h"
    K_PA_MIN = "kPa/min"
    MPA_H = "MPa/h"
    PA_H = "Pa/h"
    PA_S = "Pa/s"
    PSI_H = "psi/h"
    PSI_MIN = "psi/min"
