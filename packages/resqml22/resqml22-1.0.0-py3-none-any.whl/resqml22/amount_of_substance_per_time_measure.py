from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.amount_of_substance_per_time_uom import AmountOfSubstancePerTimeUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class AmountOfSubstancePerTimeMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[AmountOfSubstancePerTimeUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
