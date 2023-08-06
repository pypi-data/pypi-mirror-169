from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.abstract_integer_array import AbstractIntegerArray

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ElementIndices:
    """
    Index into the indexable elements selected.
    """
    supporting_representation_index: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "SupportingRepresentationIndex",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
