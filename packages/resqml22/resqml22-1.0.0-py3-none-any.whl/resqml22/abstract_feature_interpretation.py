from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.abstract_object import AbstractObject
from resqml22.abstract_time_interval import AbstractTimeInterval
from resqml22.data_object_reference import DataObjectReference
from resqml22.domain import Domain

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class AbstractFeatureInterpretation(AbstractObject):
    """
    The main class that contains all of the other feature interpretations
    included in an interpreted model.

    :ivar domain: An enumeration that specifies in which domain the
        interpretation of an AbstractFeature has been performed: depth,
        time, mixed (= depth + time )
    :ivar has_occurred_during:
    :ivar interpreted_feature:
    """
    domain: Optional[Domain] = field(
        default=None,
        metadata={
            "name": "Domain",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    has_occurred_during: Optional[AbstractTimeInterval] = field(
        default=None,
        metadata={
            "name": "HasOccurredDuring",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    interpreted_feature: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "InterpretedFeature",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
