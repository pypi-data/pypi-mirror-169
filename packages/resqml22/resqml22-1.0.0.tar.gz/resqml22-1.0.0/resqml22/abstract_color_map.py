from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.abstract_object import AbstractObject
from resqml22.hsv_color import HsvColor

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class AbstractColorMap(AbstractObject):
    null_color: Optional[HsvColor] = field(
        default=None,
        metadata={
            "name": "NullColor",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    above_max_color: Optional[HsvColor] = field(
        default=None,
        metadata={
            "name": "AboveMaxColor",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    below_min_color: Optional[HsvColor] = field(
        default=None,
        metadata={
            "name": "BelowMinColor",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
