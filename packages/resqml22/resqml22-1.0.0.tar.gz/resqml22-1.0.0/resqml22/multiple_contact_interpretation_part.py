from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from resqml22.abstract_contact_interpretation_part import AbstractContactInterpretationPart

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class MultipleContactInterpretationPart(AbstractContactInterpretationPart):
    """Describes multiple interface contacts of geologic feature-
    interpretations (compared to a binary contact).

    A composition of several contact interpretations.

    :ivar with_value: Indicates a list of binary contacts (by their
        UUIDs) that participate in this multiple-part contact.
    """
    with_value: List[int] = field(
        default_factory=list,
        metadata={
            "name": "With",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "min_occurs": 1,
            "min_inclusive": 0,
        }
    )
