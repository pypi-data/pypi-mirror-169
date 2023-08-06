from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from resqml22.address_qualifier import AddressQualifier
from resqml22.phone_type import PhoneType

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class PhoneNumberStruct:
    """A phone number with two attributes, used to "type" and "qualify" a phone
    number.

    The type would carry information such as fax, modem, voice, and the
    qualifier would carry information such as home or office.

    :ivar type: The kind of phone such as voice or fax.
    :ivar qualifier: Indicates whether the number is personal, business
        or both.
    :ivar extension: The phone number extension.
    :ivar content:
    """
    type: Optional[PhoneType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    qualifier: Optional[AddressQualifier] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    extension: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 64,
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
