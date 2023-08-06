from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


class InterpolationDomain(Enum):
    """
    Color domain/model for interpolation.

    :cvar HSV: Hue Saturation Value color model.
    :cvar RGB: Red Green Blue color model.
    """
    HSV = "hsv"
    RGB = "rgb"
