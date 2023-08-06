from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.electric_potential_difference_uom import ElectricPotentialDifferenceUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class ElectricPotentialDifferenceMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[ElectricPotentialDifferenceUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
