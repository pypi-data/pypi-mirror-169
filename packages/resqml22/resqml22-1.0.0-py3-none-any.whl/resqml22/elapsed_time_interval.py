from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.abstract_interval import AbstractInterval
from resqml22.time_measure import TimeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class ElapsedTimeInterval(AbstractInterval):
    start_elapsed_time: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "StartElapsedTime",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    end_elapsed_time: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "EndElapsedTime",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
