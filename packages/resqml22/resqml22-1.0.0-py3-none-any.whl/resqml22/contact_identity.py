from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.abstract_integer_array import AbstractIntegerArray
from resqml22.identity_kind import IdentityKind

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ContactIdentity:
    """Indicates identity between two (or more) contacts.

    For possible types of identities, see IdentityKind.

    :ivar identity_kind: The kind of contact identity. Must be one of
        the enumerations in IdentityKind.
    :ivar contact_indices: The contact representations that share common
        identity as specified by their indices.
    :ivar identical_node_indices: Indicates which nodes (identified by
        their common index in all contact representations) of the
        contact representations are identical. If this list is not
        present, then it indicates that all nodes in each representation
        are identical, on an element by element level.
    """
    identity_kind: Optional[IdentityKind] = field(
        default=None,
        metadata={
            "name": "IdentityKind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    contact_indices: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "ContactIndices",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    identical_node_indices: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "IdenticalNodeIndices",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
