from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.abstract_compound_crs import AbstractCompoundCrs
from resqml22.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class GeographicCompoundCrs(AbstractCompoundCrs):
    geographic2d_crs: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Geographic2dCrs",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
