from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from resqml22.temperature_interval_per_length_uom import TemperatureIntervalPerLengthUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class TemperatureIntervalPerLengthMeasureExt:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[Union[TemperatureIntervalPerLengthUom, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r".*:.*",
        }
    )
