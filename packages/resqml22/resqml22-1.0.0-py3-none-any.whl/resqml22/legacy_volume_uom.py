from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class LegacyVolumeUom(Enum):
    VALUE_1000SCM = "1000scm"
    VALUE_1000STB = "1000stb"
    VALUE_1_E6SCF = "1E6scf"
    VALUE_1_E6SCM = "1E6scm"
    VALUE_1_E6STB = "1E6stb"
    VALUE_1_E9SCF = "1E9scf"
    KSCF = "kscf"
    SCF = "scf"
    SCM = "scm"
    STB = "stb"
