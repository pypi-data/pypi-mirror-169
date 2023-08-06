from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


class GeologicBoundaryKind(Enum):
    """
    The various geologic boundaries a well marker can indicate.
    """
    FAULT = "fault"
    GEOBODY = "geobody"
    HORIZON = "horizon"
