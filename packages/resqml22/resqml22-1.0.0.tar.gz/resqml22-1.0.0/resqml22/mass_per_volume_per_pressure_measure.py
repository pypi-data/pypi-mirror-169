from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.mass_per_volume_per_pressure_uom import MassPerVolumePerPressureUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class MassPerVolumePerPressureMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[MassPerVolumePerPressureUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
