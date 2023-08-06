from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.abstract_parameter_key import AbstractParameterKey
from resqml22.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class ObjectParameterKey(AbstractParameterKey):
    data_object: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "DataObject",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
