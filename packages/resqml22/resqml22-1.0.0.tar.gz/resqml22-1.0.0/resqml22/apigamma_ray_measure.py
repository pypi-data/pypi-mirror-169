from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.apigamma_ray_uom import ApigammaRayUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class ApigammaRayMeasure:
    class Meta:
        name = "APIGammaRayMeasure"

    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[ApigammaRayUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
