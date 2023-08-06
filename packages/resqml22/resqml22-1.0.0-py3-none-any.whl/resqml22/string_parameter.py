from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.abstract_activity_parameter import AbstractActivityParameter

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class StringParameter(AbstractActivityParameter):
    """
    Parameter containing a string value.

    :ivar value: String value
    """
    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
            "max_length": 2000,
        }
    )
