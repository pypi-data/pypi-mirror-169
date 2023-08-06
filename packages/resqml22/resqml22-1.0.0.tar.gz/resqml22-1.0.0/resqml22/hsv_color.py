from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class HsvColor:
    """
    See https://en.wikipedia.org/wiki/HSL_and_HSV.

    :ivar alpha: Transparency/opacity of the color: 0 is totally
        transparent while 1 is totally opaque.
    :ivar hue: Hue of the color in the HSV model.
    :ivar saturation: Saturation of the color in the HSV model.
    :ivar title: Name of the color.
    :ivar value: Value of the color in the HSV model.
    """
    alpha: Optional[float] = field(
        default=None,
        metadata={
            "name": "Alpha",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    hue: Optional[float] = field(
        default=None,
        metadata={
            "name": "Hue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    saturation: Optional[float] = field(
        default=None,
        metadata={
            "name": "Saturation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "name": "Title",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    value: Optional[float] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
