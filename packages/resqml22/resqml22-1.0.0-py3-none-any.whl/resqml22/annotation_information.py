from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from resqml22.abstract_graphical_information import AbstractGraphicalInformation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class AnnotationInformation(AbstractGraphicalInformation):
    """Used for properties and property kinds and for geometry.

    In the latter case, we need to point to the representation.

    :ivar show_annotation_every: Shows the annotation (i.e., the value)
        on some of the indexable element on a regular basis.
    :ivar value_vector_indices: Especially useful for vector property
        and for geometry.
    """
    show_annotation_every: Optional[int] = field(
        default=None,
        metadata={
            "name": "ShowAnnotationEvery",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    value_vector_indices: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ValueVectorIndices",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "min_occurs": 1,
        }
    )
