from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


class DepositionalEnvironmentKind(Enum):
    CONTINENTAL = "continental"
    PARALIC_SHALLOW_MARINE = "paralic shallow marine"
    DEEP_MARINE = "deep marine"
    CARBONATE_CONTINENTAL = "carbonate continental"
    CARBONATE_PARALIC_SHALLOW_MARINE = "carbonate paralic shallow marine"
    CARBONATE_DEEP_MARINE = "carbonate deep marine"
