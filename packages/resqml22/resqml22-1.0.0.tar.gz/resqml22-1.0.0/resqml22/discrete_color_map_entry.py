from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.hsv_color import HsvColor

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class DiscreteColorMapEntry:
    """
    An association between a single integer value and a color.

    :ivar index: The integer value to be associated with a particular
        color.
    :ivar hsv:
    """
    index: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    hsv: Optional[HsvColor] = field(
        default=None,
        metadata={
            "name": "Hsv",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
