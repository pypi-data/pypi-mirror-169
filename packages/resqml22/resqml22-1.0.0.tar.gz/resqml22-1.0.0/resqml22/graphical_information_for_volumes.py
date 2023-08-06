from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.abstract_graphical_information_for_indexable_element import AbstractGraphicalInformationForIndexableElement

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class GraphicalInformationForVolumes(AbstractGraphicalInformationForIndexableElement):
    """
    Graphical information for volumes.

    :ivar use_interpolation_between_nodes: Interpolate the values all
        along the volume based on a fixed value set on nodes.
    """
    use_interpolation_between_nodes: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UseInterpolationBetweenNodes",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
