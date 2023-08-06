from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.logarithmic_power_ratio_per_length_uom import LogarithmicPowerRatioPerLengthUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class LogarithmicPowerRatioPerLengthMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[LogarithmicPowerRatioPerLengthUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
