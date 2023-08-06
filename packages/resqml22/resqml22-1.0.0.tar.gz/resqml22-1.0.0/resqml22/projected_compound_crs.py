from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.abstract_compound_crs import AbstractCompoundCrs
from resqml22.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class ProjectedCompoundCrs(AbstractCompoundCrs):
    projected_crs: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "ProjectedCrs",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
