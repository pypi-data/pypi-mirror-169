from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.dimensionless_uom import DimensionlessUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class DimensionlessMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[DimensionlessUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
