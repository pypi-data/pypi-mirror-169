from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.abstract_graphical_information import AbstractGraphicalInformation
from resqml22.data_object_reference import DataObjectReference
from resqml22.min_max import MinMax

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ColorInformation(AbstractGraphicalInformation):
    """Used for properties and property kinds and for geometry.

    In the latter case, we need to point to the representation.

    :ivar min_max: This is the range of values of the associated
        property which will result in the minimum color and the maximum
        color. This is not necessarily the entire range of values of the
        data - data outside this range will continue to have the extreme
        color from this range.
    :ivar use_logarithmic_mapping: Indicates that the log of the
        property values are taken into account when mapped with the
        index of the color map.
    :ivar use_reverse_mapping: Indicates that the minimum value of the
        property corresponds to the maximum index of the color map and
        that the maximum value of the property corresponds to the
        minimum index of the color map.
    :ivar value_vector_index: Especially useful for vectorial property
        and for geometry.
    :ivar color_map:
    """
    min_max: Optional[MinMax] = field(
        default=None,
        metadata={
            "name": "MinMax",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    use_logarithmic_mapping: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UseLogarithmicMapping",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    use_reverse_mapping: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UseReverseMapping",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
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
    color_map: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "ColorMap",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
