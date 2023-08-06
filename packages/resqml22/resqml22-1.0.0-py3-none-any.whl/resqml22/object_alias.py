from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from resqml22.alias_identifier_kind import AliasIdentifierKind

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class ObjectAlias:
    """Use this to create multiple aliases for any object instance.

    Note that an Authority is required for each alias.

    :ivar identifier:
    :ivar identifier_kind:
    :ivar description:
    :ivar effective_date_time: The date and time when an alias name
        became effective.
    :ivar termination_date_time: The data and time when an alias name
        ceased to be effective.
    :ivar authority:
    """
    identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "Identifier",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
            "max_length": 64,
        }
    )
    identifier_kind: Optional[Union[AliasIdentifierKind, str]] = field(
        default=None,
        metadata={
            "name": "IdentifierKind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "pattern": r".*:.*",
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "max_length": 2000,
        }
    )
    effective_date_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "EffectiveDateTime",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    termination_date_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "TerminationDateTime",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    authority: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 64,
        }
    )
