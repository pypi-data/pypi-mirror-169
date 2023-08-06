from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from resqml22.reciprocal_area_uom import ReciprocalAreaUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class ReciprocalAreaMeasureExt:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[Union[ReciprocalAreaUom, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r".*:.*",
        }
    )
