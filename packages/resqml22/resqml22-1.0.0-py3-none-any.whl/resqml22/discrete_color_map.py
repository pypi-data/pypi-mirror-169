from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from resqml22.abstract_color_map import AbstractColorMap
from resqml22.discrete_color_map_entry import DiscreteColorMapEntry

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class DiscreteColorMap(AbstractColorMap):
    """A color map associating an integer value to a color.

    BUSINESS RULE: When using a discrete color map for a continuous
    property the property value will be equal to the next lowest integer
    in the color map.  For example a color map of 10, 20, 30, etc., and
    a continuous property value of 16.5 will result in a value of 10 for
    the minimum.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    entry: List[DiscreteColorMapEntry] = field(
        default_factory=list,
        metadata={
            "name": "Entry",
            "type": "Element",
            "min_occurs": 1,
        }
    )
