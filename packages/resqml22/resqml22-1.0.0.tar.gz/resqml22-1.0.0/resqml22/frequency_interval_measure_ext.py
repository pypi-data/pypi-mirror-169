from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from resqml22.frequency_interval_uom import FrequencyIntervalUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class FrequencyIntervalMeasureExt:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[Union[FrequencyIntervalUom, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r".*:.*",
        }
    )
