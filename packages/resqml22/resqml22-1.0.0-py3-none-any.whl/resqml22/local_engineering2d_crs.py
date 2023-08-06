from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.cartesian2d_crs import Cartesian2DCrs
from resqml22.horizontal_axes import HorizontalAxes
from resqml22.north_reference_kind import NorthReferenceKind
from resqml22.plane_angle_measure_ext import PlaneAngleMeasureExt
from resqml22.projected_crs import ProjectedCrs

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class LocalEngineering2DCrs(Cartesian2DCrs):
    class Meta:
        name = "LocalEngineering2dCrs"
        namespace = "http://www.energistics.org/energyml/data/commonv2"

    azimuth: Optional[PlaneAngleMeasureExt] = field(
        default=None,
        metadata={
            "name": "Azimuth",
            "type": "Element",
            "required": True,
        }
    )
    azimuth_reference: Optional[NorthReferenceKind] = field(
        default=None,
        metadata={
            "name": "AzimuthReference",
            "type": "Element",
            "required": True,
        }
    )
    origin_projected_coordinate1: Optional[float] = field(
        default=None,
        metadata={
            "name": "OriginProjectedCoordinate1",
            "type": "Element",
            "required": True,
        }
    )
    origin_projected_coordinate2: Optional[float] = field(
        default=None,
        metadata={
            "name": "OriginProjectedCoordinate2",
            "type": "Element",
            "required": True,
        }
    )
    horizontal_axes: Optional[HorizontalAxes] = field(
        default=None,
        metadata={
            "name": "HorizontalAxes",
            "type": "Element",
            "required": True,
        }
    )
    origin_projected_crs: Optional[ProjectedCrs] = field(
        default=None,
        metadata={
            "name": "OriginProjectedCrs",
            "type": "Element",
            "required": True,
        }
    )
