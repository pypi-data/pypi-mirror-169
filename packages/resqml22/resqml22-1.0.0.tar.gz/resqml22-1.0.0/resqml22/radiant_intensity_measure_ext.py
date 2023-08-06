from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from resqml22.radiant_intensity_uom import RadiantIntensityUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class RadiantIntensityMeasureExt:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[Union[RadiantIntensityUom, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r".*:.*",
        }
    )
