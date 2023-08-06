from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.activity_of_radioactivity_per_volume_uom import ActivityOfRadioactivityPerVolumeUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class ActivityOfRadioactivityPerVolumeMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[ActivityOfRadioactivityPerVolumeUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
