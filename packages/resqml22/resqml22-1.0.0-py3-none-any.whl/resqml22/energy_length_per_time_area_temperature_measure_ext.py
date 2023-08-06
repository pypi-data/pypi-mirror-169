from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from resqml22.energy_length_per_time_area_temperature_uom import EnergyLengthPerTimeAreaTemperatureUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class EnergyLengthPerTimeAreaTemperatureMeasureExt:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[Union[EnergyLengthPerTimeAreaTemperatureUom, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r".*:.*",
        }
    )
