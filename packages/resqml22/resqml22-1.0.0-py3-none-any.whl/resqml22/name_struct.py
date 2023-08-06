from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class NameStruct:
    """
    The name of something within a naming system.

    :ivar value:
    :ivar authority: The authority for the naming system, e.g., a
        company.
    """
    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 64,
        }
    )
    authority: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 64,
        }
    )
