from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from resqml22.abstract_object import AbstractObject
from resqml22.property_kind import PropertyKind

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class PropertyKindDictionary(AbstractObject):
    """
    This dictionary defines property kind which is intended to handle the
    requirements of the upstream oil and gas industry.

    :ivar property_kind: Defines which property kind are contained into
        a property kind dictionary.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/commonv2"

    property_kind: List[PropertyKind] = field(
        default_factory=list,
        metadata={
            "name": "PropertyKind",
            "type": "Element",
            "min_occurs": 2,
        }
    )
