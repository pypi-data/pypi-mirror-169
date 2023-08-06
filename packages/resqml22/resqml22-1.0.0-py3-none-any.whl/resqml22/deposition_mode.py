from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


class DepositionMode(Enum):
    """
    Specifies the position of the stratification of a stratigraphic unit with
    respect to its top and bottom boundaries.
    """
    PROPORTIONAL_BETWEEN_TOP_AND_BOTTOM = "proportional between top and bottom"
    PARALLEL_TO_BOTTOM = "parallel to bottom"
    PARALLEL_TO_TOP = "parallel to top"
    PARALLEL_TO_ANOTHER_BOUNDARY = "parallel to another boundary"
