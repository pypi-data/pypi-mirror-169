from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.abstract_feature_interpretation import AbstractFeatureInterpretation
from resqml22.geologic_time import GeologicTime

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class BoundaryFeatureInterpretation(AbstractFeatureInterpretation):
    """The main class for data describing an opinion of a surface feature
    between two volumes.

    BUSINESS RULE: The data-object reference (of type "interprets") must
    reference only a boundary feature.

    :ivar older_possible_age: A value in years of the age offset between
        the DateTime attribute value and the DateTime of a
        GeologicalEvent occurrence of generation. When it represents a
        geological event that happened in the past, this value must be
        POSITIVE.
    :ivar younger_possible_age: A value in years of the age offset
        between the DateTime attribute value and the DateTime of a
        GeologicalEvent occurrence of generation. When it represents a
        geological event that happened in the past, this value must be
        POSITIVE.
    :ivar absolute_age:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    older_possible_age: Optional[int] = field(
        default=None,
        metadata={
            "name": "OlderPossibleAge",
            "type": "Element",
        }
    )
    younger_possible_age: Optional[int] = field(
        default=None,
        metadata={
            "name": "YoungerPossibleAge",
            "type": "Element",
        }
    )
    absolute_age: Optional[GeologicTime] = field(
        default=None,
        metadata={
            "name": "AbsoluteAge",
            "type": "Element",
        }
    )
