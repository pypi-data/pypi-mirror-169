from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.electric_current_density_uom import ElectricCurrentDensityUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class ElectricCurrentDensityMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[ElectricCurrentDensityUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
