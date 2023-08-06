from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from resqml22.abstract_geometry import AbstractGeometry
from resqml22.abstract_surface_framework_contact import AbstractSurfaceFrameworkContact
from resqml22.contact_patch import ContactPatch

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class NonSealedContact(AbstractSurfaceFrameworkContact):
    """
    Defines a non-sealed contact representation, meaning that this contact
    representation is defined by a geometry.
    """
    patches: List[ContactPatch] = field(
        default_factory=list,
        metadata={
            "name": "Patches",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    geometry: Optional[AbstractGeometry] = field(
        default=None,
        metadata={
            "name": "Geometry",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
