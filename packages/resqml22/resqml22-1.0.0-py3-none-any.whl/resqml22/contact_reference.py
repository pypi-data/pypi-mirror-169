from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.abstract_surface_framework_contact import AbstractSurfaceFrameworkContact
from resqml22.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ContactReference(AbstractSurfaceFrameworkContact):
    """
    Used when the contact already exists as a top-level element representation.
    """
    representation: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Representation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
