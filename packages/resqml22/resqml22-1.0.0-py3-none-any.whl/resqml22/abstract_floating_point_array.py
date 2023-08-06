from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from resqml22.abstract_numeric_array import AbstractNumericArray
from resqml22.floating_point_array_statistics import FloatingPointArrayStatistics

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class AbstractFloatingPointArray(AbstractNumericArray):
    """Generic representation of an array of double values.

    Each derived element provides specialized implementation to allow
    specific optimization of the representation.
    """
    statistics: List[FloatingPointArrayStatistics] = field(
        default_factory=list,
        metadata={
            "name": "Statistics",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
        }
    )
