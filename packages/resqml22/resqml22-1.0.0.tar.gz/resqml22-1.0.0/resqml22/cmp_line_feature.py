from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.abstract_integer_array import AbstractIntegerArray
from resqml22.abstract_seismic_line_feature import AbstractSeismicLineFeature
from resqml22.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class CmpLineFeature(AbstractSeismicLineFeature):
    """
    Location of a single line of common mid-points (CMP) resulting from a 2D
    seismic acquisition.

    :ivar nearest_shot_point_indices: Index of closest shot point
        (inside the associated CmpPointLineFeature) for each cmp.
    :ivar shot_point_line_feature:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    nearest_shot_point_indices: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "NearestShotPointIndices",
            "type": "Element",
            "required": True,
        }
    )
    shot_point_line_feature: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "ShotPointLineFeature",
            "type": "Element",
        }
    )
