from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from resqml22.volume_per_time_per_pressure_length_uom import VolumePerTimePerPressureLengthUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class VolumePerTimePerPressureLengthMeasureExt:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[Union[VolumePerTimePerPressureLengthUom, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r".*:.*",
        }
    )
