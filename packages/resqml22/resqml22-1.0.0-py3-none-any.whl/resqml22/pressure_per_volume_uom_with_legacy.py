from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class PressurePerVolumeUomWithLegacy(Enum):
    """
    :cvar PA_SCM:
    :cvar PSI_1000SCF:
    :cvar PSI_1_E6SCF:
    :cvar PA_M3: pascal per cubic metre
    :cvar PSI2_D_C_P_FT3: psi squared day per centipoise cubic foot
    """
    PA_SCM = "Pa/scm"
    PSI_1000SCF = "psi/1000scf"
    PSI_1_E6SCF = "psi/1E6scf"
    PA_M3 = "Pa/m3"
    PSI2_D_C_P_FT3 = "psi2.d/(cP.ft3)"
