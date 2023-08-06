from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from resqml22.abstract_color_map import AbstractColorMap
from resqml22.abstract_object import AbstractObject

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ColorMapDictionary(AbstractObject):
    """
    A container for color maps.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    color_map: List[AbstractColorMap] = field(
        default_factory=list,
        metadata={
            "name": "ColorMap",
            "type": "Element",
        }
    )
