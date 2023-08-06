from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.heat_flow_rate_uom import HeatFlowRateUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class HeatFlowRateMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[HeatFlowRateUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
