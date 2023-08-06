from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from resqml22.abstract_string_array import AbstractStringArray

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class StringXmlArray(AbstractStringArray):
    count_per_value: int = field(
        default=1,
        metadata={
            "name": "CountPerValue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    values: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Values",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "min_occurs": 1,
        }
    )
