from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from resqml22.area_per_amount_of_substance_uom import AreaPerAmountOfSubstanceUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class AreaPerAmountOfSubstanceMeasureExt:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[Union[AreaPerAmountOfSubstanceUom, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r".*:.*",
        }
    )
