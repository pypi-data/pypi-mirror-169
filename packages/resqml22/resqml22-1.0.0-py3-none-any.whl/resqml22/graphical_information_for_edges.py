from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from resqml22.abstract_graphical_information_for_indexable_element import AbstractGraphicalInformationForIndexableElement
from resqml22.display_space import DisplaySpace
from resqml22.edge_pattern import EdgePattern
from resqml22.length_measure_ext import LengthMeasureExt

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class GraphicalInformationForEdges(AbstractGraphicalInformationForIndexableElement):
    """
    Graphical information for edges.

    :ivar display_space:
    :ivar pattern: The pattern of the edge.
    :ivar thickness: The thickness of the edge.
    :ivar use_interpolation_between_nodes: Use color and size
        interpolation between nodes.
    """
    display_space: Optional[DisplaySpace] = field(
        default=None,
        metadata={
            "name": "DisplaySpace",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    pattern: Optional[Union[EdgePattern, str]] = field(
        default=None,
        metadata={
            "name": "Pattern",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "pattern": r".*:.*",
        }
    )
    thickness: Optional[LengthMeasureExt] = field(
        default=None,
        metadata={
            "name": "Thickness",
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
