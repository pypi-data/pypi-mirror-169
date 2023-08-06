from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from resqml22.logarithmic_power_ratio_per_length_uom import LogarithmicPowerRatioPerLengthUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class LogarithmicPowerRatioPerLengthMeasureExt:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[Union[LogarithmicPowerRatioPerLengthUom, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r".*:.*",
        }
    )
