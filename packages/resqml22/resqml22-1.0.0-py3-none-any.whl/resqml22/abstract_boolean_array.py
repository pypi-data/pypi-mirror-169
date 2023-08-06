from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from resqml22.abstract_value_array import AbstractValueArray
from resqml22.boolean_array_statistics import BooleanArrayStatistics

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class AbstractBooleanArray(AbstractValueArray):
    """Generic representation of an array of Boolean values.

    Each derived element provides a specialized implementation to allow
    specific optimization of the representation.
    """
    statistics: List[BooleanArrayStatistics] = field(
        default_factory=list,
        metadata={
            "name": "Statistics",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
        }
    )
