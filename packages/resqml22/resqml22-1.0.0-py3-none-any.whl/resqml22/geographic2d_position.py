from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.abstract2d_position import Abstract2DPosition
from resqml22.data_object_reference import DataObjectReference
from resqml22.plane_angle_measure_ext import PlaneAngleMeasureExt

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class Geographic2DPosition(Abstract2DPosition):
    class Meta:
        name = "Geographic2dPosition"

    latitude: Optional[PlaneAngleMeasureExt] = field(
        default=None,
        metadata={
            "name": "Latitude",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    longitude: Optional[PlaneAngleMeasureExt] = field(
        default=None,
        metadata={
            "name": "Longitude",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    epoch: Optional[float] = field(
        default=None,
        metadata={
            "name": "Epoch",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
        }
    )
    geographic_crs: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "GeographicCrs",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
