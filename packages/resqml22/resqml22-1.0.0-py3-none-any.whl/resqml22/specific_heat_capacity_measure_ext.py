from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from resqml22.specific_heat_capacity_uom import SpecificHeatCapacityUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class SpecificHeatCapacityMeasureExt:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[Union[SpecificHeatCapacityUom, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r".*:.*",
        }
    )
