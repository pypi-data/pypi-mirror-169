from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from resqml22.amount_of_substance_per_time_per_area_uom import AmountOfSubstancePerTimePerAreaUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class AmountOfSubstancePerTimePerAreaMeasureExt:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[Union[AmountOfSubstancePerTimePerAreaUom, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r".*:.*",
        }
    )
