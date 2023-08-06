from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from resqml22.energy_per_mass_per_time_uom import EnergyPerMassPerTimeUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class EnergyPerMassPerTimeMeasureExt:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[Union[EnergyPerMassPerTimeUom, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r".*:.*",
        }
    )
