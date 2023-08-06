from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from resqml22.absorbed_dose_uom import AbsorbedDoseUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class AbsorbedDoseMeasureExt:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[Union[AbsorbedDoseUom, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r".*:.*",
        }
    )
