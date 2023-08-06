from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from resqml22.diffusion_coefficient_uom import DiffusionCoefficientUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class DiffusionCoefficientMeasureExt:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[Union[DiffusionCoefficientUom, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r".*:.*",
        }
    )
