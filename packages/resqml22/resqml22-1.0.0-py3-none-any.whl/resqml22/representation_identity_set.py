from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from resqml22.abstract_object import AbstractObject
from resqml22.representation_identity import RepresentationIdentity

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class RepresentationIdentitySet(AbstractObject):
    """
    A collection of representation identities.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    representation_identity: List[RepresentationIdentity] = field(
        default_factory=list,
        metadata={
            "name": "RepresentationIdentity",
            "type": "Element",
            "min_occurs": 1,
        }
    )
