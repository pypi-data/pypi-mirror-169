from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from resqml22.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class MarkerInterval:
    organization: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Organization",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    interpretation: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "Interpretation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
