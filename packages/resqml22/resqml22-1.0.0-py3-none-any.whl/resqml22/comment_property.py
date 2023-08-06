from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.abstract_values_property import AbstractValuesProperty

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class CommentProperty(AbstractValuesProperty):
    """Information specific to one comment property.

    Used to capture comments or annotations associated with a given
    element type in a data-object, for example, associating comments on
    the specific location of a well path.

    :ivar language: Identify the language (e.g., US English or French)
        of the string. It is recommended that language names conform to
        ISO 639.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    language: Optional[str] = field(
        default=None,
        metadata={
            "name": "Language",
            "type": "Element",
            "max_length": 64,
        }
    )
