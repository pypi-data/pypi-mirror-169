from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class MinMax:
    """
    A simple reusable structure that carries a minimum and a maximum double
    value leading to the definition of an interval of values.

    :ivar minimum: The minimum value of the interval.
    :ivar maximum: The maximum value of the interval.
    """
    minimum: Optional[float] = field(
        default=None,
        metadata={
            "name": "Minimum",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    maximum: Optional[float] = field(
        default=None,
        metadata={
            "name": "Maximum",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
