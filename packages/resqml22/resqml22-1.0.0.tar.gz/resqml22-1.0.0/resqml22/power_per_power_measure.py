from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.power_per_power_uom import PowerPerPowerUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class PowerPerPowerMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[PowerPerPowerUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
