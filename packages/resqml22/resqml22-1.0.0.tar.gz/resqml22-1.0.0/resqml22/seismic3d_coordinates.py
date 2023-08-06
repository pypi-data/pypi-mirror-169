from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.abstract_floating_point_array import AbstractFloatingPointArray
from resqml22.abstract_seismic_coordinates import AbstractSeismicCoordinates

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class Seismic3DCoordinates(AbstractSeismicCoordinates):
    """
    The 1-to-1 mapping between geometry coordinates (usually X, Y, Z or X, Y,
    TWT) and trace or inter-trace positions on a seismic lattice.

    :ivar crossline_coordinates: The sequence of trace or inter-trace
        crossline positions that correspond to the geometry coordinates.
        BUSINESS RULE: Both sequences must be in the same order.
    :ivar inline_coordinates: The sequence of trace or inter-trace
        inline positions that correspond to the geometry coordinates.
        BUSINESS RULE: Both sequences must be in the same order.
    :ivar vertical_coordinates: The sequence of vertical sample or
        inter-sample positions that corresponds to the geometry
        coordinates. BUSINESS RULE: Sequence must be in the same order
        as the two previous ones.
    """
    class Meta:
        name = "Seismic3dCoordinates"

    crossline_coordinates: Optional[AbstractFloatingPointArray] = field(
        default=None,
        metadata={
            "name": "CrosslineCoordinates",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    inline_coordinates: Optional[AbstractFloatingPointArray] = field(
        default=None,
        metadata={
            "name": "InlineCoordinates",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    vertical_coordinates: Optional[AbstractFloatingPointArray] = field(
        default=None,
        metadata={
            "name": "VerticalCoordinates",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
