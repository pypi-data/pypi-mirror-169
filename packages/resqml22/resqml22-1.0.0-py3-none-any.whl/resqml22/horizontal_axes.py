from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from resqml22.axis_direction_kind import AxisDirectionKind
from resqml22.length_uom import LengthUom
from resqml22.time_uom import TimeUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class HorizontalAxes:
    """
    :ivar direction1: Direction of the axis. Commonly used for values
        such as "easting, northing, depth, etc.."
    :ivar direction2:
    :ivar uom:
    :ivar is_time:
    """
    direction1: Optional[AxisDirectionKind] = field(
        default=None,
        metadata={
            "name": "Direction1",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    direction2: Optional[AxisDirectionKind] = field(
        default=None,
        metadata={
            "name": "Direction2",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    uom: Optional[Union[LengthUom, TimeUom, str]] = field(
        default=None,
        metadata={
            "name": "Uom",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
            "pattern": r".*:.*",
        }
    )
    is_time: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsTime",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
