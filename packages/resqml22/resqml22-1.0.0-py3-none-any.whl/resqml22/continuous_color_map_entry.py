from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.hsv_color import HsvColor

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ContinuousColorMapEntry:
    """
    An association between a single double value and a color.

    :ivar index: The double value to be associated with a particular
        color.
    :ivar hsv:
    """
    index: Optional[float] = field(
        default=None,
        metadata={
            "name": "Index",
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
