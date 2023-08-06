from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.abstract_graphical_information_for_indexable_element import AbstractGraphicalInformationForIndexableElement

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class GraphicalInformationForFaces(AbstractGraphicalInformationForIndexableElement):
    """
    Graphical information for faces.

    :ivar applies_on_right_handed_face: If true the graphical
        information only applies to the right handed side of the face.
        If false, it only applies to the left handed side of the face.
        If not present the graphical information applies to both sides
        of faces.
    :ivar use_interpolation_between_nodes: Interpolate the values all
        along the face based on fixed value set on nodes.
    """
    applies_on_right_handed_face: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AppliesOnRightHandedFace",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    use_interpolation_between_nodes: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UseInterpolationBetweenNodes",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
