from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.abstract2d_crs import Abstract2DCrs
from resqml22.abstract_geographic2d_crs import AbstractGeographic2DCrs

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class Geographic2DCrs(Abstract2DCrs):
    class Meta:
        name = "Geographic2dCrs"
        namespace = "http://www.energistics.org/energyml/data/commonv2"

    abstract_geographic2d_crs: Optional[AbstractGeographic2DCrs] = field(
        default=None,
        metadata={
            "name": "AbstractGeographic2dCrs",
            "type": "Element",
            "required": True,
        }
    )
