from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.abstract_horizontal_coordinates import AbstractHorizontalCoordinates
from resqml22.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class ProjectedCoordinates(AbstractHorizontalCoordinates):
    crs: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Crs",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
