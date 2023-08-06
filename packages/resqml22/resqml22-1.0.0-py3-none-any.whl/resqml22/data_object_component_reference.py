from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from resqml22.component_reference import ComponentReference
from resqml22.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class DataObjectComponentReference:
    """
    A pointer to a component within another Energistics data object.

    :ivar data_object: The data object containing the component.
    :ivar component: A component within the data object that is being
        referenced by its UID. If more than one Component is included,
        it is a reference to a component that is nested within the
        previous component.
    """
    data_object: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "DataObject",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    component: List[ComponentReference] = field(
        default_factory=list,
        metadata={
            "name": "Component",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "min_occurs": 1,
        }
    )
