from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from resqml22.reciprocal_electric_potential_difference_uom import ReciprocalElectricPotentialDifferenceUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class ReciprocalElectricPotentialDifferenceMeasureExt:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[Union[ReciprocalElectricPotentialDifferenceUom, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r".*:.*",
        }
    )
