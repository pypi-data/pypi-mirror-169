from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class LegacyPressurePerVolumeUom(Enum):
    PA_SCM = "Pa/scm"
    PSI_1000SCF = "psi/1000scf"
    PSI_1_E6SCF = "psi/1E6scf"
