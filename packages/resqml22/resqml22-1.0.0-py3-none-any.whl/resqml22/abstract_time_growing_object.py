from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.abstract_growing_object import AbstractGrowingObject
from resqml22.date_time_interval import DateTimeInterval

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class AbstractTimeGrowingObject(AbstractGrowingObject):
    """
    A growing object where the parts are of type eml:AbstractTimeGrowingPart or
    eml:AbstractTimeIntervalGrowingPart.

    :ivar time_interval: The time interval for the parts in this growing
        object. StartTime MUST equal the minimum time of any part
        (interval). EndTime MUST equal the maximum time of any part
        (interval). In an ETP store, the interval values are managed by
        the store. This MUST be specified when there are parts in the
        object, and it MUST NOT be specified when there are no parts in
        the object.
    """
    time_interval: Optional[DateTimeInterval] = field(
        default=None,
        metadata={
            "name": "TimeInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
        }
    )
