from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from resqml22.abstract_color_map import AbstractColorMap
from resqml22.continuous_color_map_entry import ContinuousColorMapEntry
from resqml22.interpolation_domain import InterpolationDomain
from resqml22.interpolation_method import InterpolationMethod

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ContinuousColorMap(AbstractColorMap):
    """
    A color map associating a double value to a color.

    :ivar interpolation_domain: The domain for the interpolation between
        color map entries.
    :ivar interpolation_method: The method for the interpolation between
        color map entries.
    :ivar entry:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    interpolation_domain: Optional[InterpolationDomain] = field(
        default=None,
        metadata={
            "name": "InterpolationDomain",
            "type": "Element",
            "required": True,
        }
    )
    interpolation_method: Optional[InterpolationMethod] = field(
        default=None,
        metadata={
            "name": "InterpolationMethod",
            "type": "Element",
            "required": True,
        }
    )
    entry: List[ContinuousColorMapEntry] = field(
        default_factory=list,
        metadata={
            "name": "Entry",
            "type": "Element",
            "min_occurs": 2,
        }
    )
