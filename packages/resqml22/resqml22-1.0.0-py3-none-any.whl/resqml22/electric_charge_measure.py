from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.electric_charge_uom import ElectricChargeUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class ElectricChargeMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[ElectricChargeUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
