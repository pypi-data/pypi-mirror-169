from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class AbstractContactInterpretationPart:
    """The parent class of an atomic, linear, or surface geologic contact
    description.

    When the contact is between two surface representations (e.g.,
    fault/fault, horizon/fault, horizon/horizon), then the contact is a
    line. When the contact is between two volume representations
    (stratigraphic unit/stratigraphic unit), then the contact is a
    surface. A contact interpretation can be associated with other
    contact interpretations in an organization interpretation. To define
    a contact representation, you must first define a contact
    interpretation.
    """
    part_of: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "PartOf",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
