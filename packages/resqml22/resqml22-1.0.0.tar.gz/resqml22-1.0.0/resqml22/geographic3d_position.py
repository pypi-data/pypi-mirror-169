from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.abstract3d_position import Abstract3DPosition
from resqml22.geographic3d_crs import Geographic3DCrs

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class Geographic3DPosition(Abstract3DPosition):
    class Meta:
        name = "Geographic3dPosition"

    latitude: Optional[float] = field(
        default=None,
        metadata={
            "name": "Latitude",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    longitude: Optional[float] = field(
        default=None,
        metadata={
            "name": "Longitude",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    ellipsoidal_height: Optional[float] = field(
        default=None,
        metadata={
            "name": "EllipsoidalHeight",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    geographic3d_crs: Optional[Geographic3DCrs] = field(
        default=None,
        metadata={
            "name": "Geographic3dCrs",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
