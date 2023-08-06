from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.abstract_graphical_information_for_indexable_element import AbstractGraphicalInformationForIndexableElement

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class GraphicalInformationForWholeObject(AbstractGraphicalInformationForIndexableElement):
    """
    Graphical information for the whole data object.

    :ivar active_contour_line_set_information_index: Display the contour
        line of the visualized data object according to information at a
        particular index of the GraphicalInformationSet.
    :ivar display_title: Display the title of the visualized data object
        next to it.
    """
    active_contour_line_set_information_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "ActiveContourLineSetInformationIndex",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    display_title: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DisplayTitle",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
