from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


class SequenceStratigraphySurfaceKind(Enum):
    """
    The enumerated attributes of a horizon.
    """
    FLOODING = "flooding"
    MAXIMUM_FLOODING = "maximum flooding"
    REGRESSIVE = "regressive"
    MAXIMUM_REGRESSIVE = "maximum regressive"
    TRANSGRESSIVE = "transgressive"
    MAXIMUM_TRANSGRESSIVE = "maximum transgressive"
    ABANDONMENT = "abandonment"
    CORRELATIVE_CONFORMITY = "correlative conformity"
    RAVINEMENT = "ravinement"
    SEQUENCE_BOUNDARY = "sequence boundary"
