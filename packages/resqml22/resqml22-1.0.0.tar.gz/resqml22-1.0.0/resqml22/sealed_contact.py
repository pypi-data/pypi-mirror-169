from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from resqml22.abstract_integer_array import AbstractIntegerArray
from resqml22.abstract_surface_framework_contact import AbstractSurfaceFrameworkContact
from resqml22.contact_patch import ContactPatch
from resqml22.identity_kind import IdentityKind

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class SealedContact(AbstractSurfaceFrameworkContact):
    """Sealed contact elements that indicate that 2 or more contact patches are
    partially or totally colocated or equivalent.

    For possible types of identity, see IdentityKind.

    :ivar identical_node_indices: Indicates which nodes (identified by
        their common index in all contact patches) of the contact
        patches are identical. If this list is not present, then it
        indicates that all nodes in each representation are identical,
        on an element-by-element level.
    :ivar identity_kind: Must be one of the enumerations in
        IdentityKind.
    :ivar patches:
    """
    identical_node_indices: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "IdenticalNodeIndices",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    identity_kind: Optional[IdentityKind] = field(
        default=None,
        metadata={
            "name": "IdentityKind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    patches: List[ContactPatch] = field(
        default_factory=list,
        metadata={
            "name": "Patches",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "min_occurs": 2,
        }
    )
