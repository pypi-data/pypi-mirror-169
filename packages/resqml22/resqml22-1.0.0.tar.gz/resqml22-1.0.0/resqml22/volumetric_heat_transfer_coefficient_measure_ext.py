from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from resqml22.volumetric_heat_transfer_coefficient_uom import VolumetricHeatTransferCoefficientUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class VolumetricHeatTransferCoefficientMeasureExt:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[Union[VolumetricHeatTransferCoefficientUom, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r".*:.*",
        }
    )
