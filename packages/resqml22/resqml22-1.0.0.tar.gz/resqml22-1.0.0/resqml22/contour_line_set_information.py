from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.abstract_graphical_information import AbstractGraphicalInformation
from resqml22.graphical_information_for_edges import GraphicalInformationForEdges

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ContourLineSetInformation(AbstractGraphicalInformation):
    """
    Information about contour lines between regions having different ranges of
    values (elevation or depth mostly).

    :ivar display_label_on_major_line: Indicator to display the contour
        line value on major lines. To differentiate minor and major
        lines, see ShowMajorLineEvery.
    :ivar display_label_on_minor_line: Indicator to display the contour
        line value on minor lines. To differentiate minor and major
        lines, see ShowMajorLineEvery.
    :ivar increment: The absolute incremented value between two
        consecutive minor contour lines.
    :ivar major_line_graphical_information: Graphical information of
        major lines.
    :ivar minor_line_graphical_information: Graphical information of
        minor lines.
    :ivar show_major_line_every: Allows to regularly promote some minor
        lines to major lines.
    :ivar value_vector_index: Especially useful for vectorial property
        and for geometry.
    """
    display_label_on_major_line: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DisplayLabelOnMajorLine",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    display_label_on_minor_line: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DisplayLabelOnMinorLine",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    increment: Optional[float] = field(
        default=None,
        metadata={
            "name": "Increment",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    major_line_graphical_information: Optional[GraphicalInformationForEdges] = field(
        default=None,
        metadata={
            "name": "MajorLineGraphicalInformation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    minor_line_graphical_information: Optional[GraphicalInformationForEdges] = field(
        default=None,
        metadata={
            "name": "MinorLineGraphicalInformation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    show_major_line_every: Optional[int] = field(
        default=None,
        metadata={
            "name": "ShowMajorLineEvery",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    value_vector_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "ValueVectorIndex",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
