from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class AmountOfSubstancePerTimeUom(Enum):
    """
    :cvar KAT: katal
    :cvar KMOL_H: kilogram-mole per hour
    :cvar KMOL_S: kilogram-mole per second
    :cvar LBMOL_H: pound-mass-mole per hour
    :cvar LBMOL_S: pound-mass-mole per second
    :cvar MOL_S: gram-mole per second
    """
    KAT = "kat"
    KMOL_H = "kmol/h"
    KMOL_S = "kmol/s"
    LBMOL_H = "lbmol/h"
    LBMOL_S = "lbmol/s"
    MOL_S = "mol/s"
