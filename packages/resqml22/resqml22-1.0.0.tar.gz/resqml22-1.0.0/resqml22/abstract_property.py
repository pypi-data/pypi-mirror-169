from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from resqml22.abstract_integer_array import AbstractIntegerArray
from resqml22.abstract_object import AbstractObject
from resqml22.data_object_reference import DataObjectReference
from resqml22.geologic_time import GeologicTime
from resqml22.indexable_element import IndexableElement
from resqml22.time_or_interval_series import TimeOrIntervalSeries

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class AbstractProperty(AbstractObject):
    """Base class for storing all property values on representations, except
    current geometry location.

    Values attached to a given element can be either a scalar or a
    vector. The size of the vector is constant on all elements, and it
    is assumed that all elements of the vector have identical property
    types and share the same unit of measure.

    :ivar indexable_element:
    :ivar time:
    :ivar realization_indices: Provide the list of indices corresponding
        to realizations number. For example, if a user wants to send the
        realization corresponding to p10, p20, ... he would write the
        array 10, 20, ... If not provided, then the realization count
        (which could be 1) does not introduce a dimension to the multi-
        dimensional array storage.
    :ivar value_count_per_indexable_element: The count of value in one
        dimension for each indexable element. It is ordered as the
        values are ordered in the data set. REMINDER: First (left) given
        dimension is slowest and last (right) given dimension is
        fastest. The top XML element is slower than the bottom.
    :ivar property_kind: Pointer to a PropertyKind.  The Energistics
        dictionary can be found at
        http://w3.energistics.org/energyML/data/common/v2.1/ancillary/PropertyKindDictionary_v2.1.0.xml.
    :ivar label_per_component: Labels for each component of a vector or
        tensor property in a linearized way. REMINDER: First (left)
        given dimension is slowest and last (right) given dimension is
        fastest.
    :ivar supporting_representation:
    :ivar local_crs:
    :ivar time_or_interval_series:
    """
    indexable_element: Optional[IndexableElement] = field(
        default=None,
        metadata={
            "name": "IndexableElement",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    time: Optional[GeologicTime] = field(
        default=None,
        metadata={
            "name": "Time",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    realization_indices: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "RealizationIndices",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    value_count_per_indexable_element: List[int] = field(
        default_factory=list,
        metadata={
            "name": "ValueCountPerIndexableElement",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "min_occurs": 1,
            "min_inclusive": 1,
        }
    )
    property_kind: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "PropertyKind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    label_per_component: List[str] = field(
        default_factory=list,
        metadata={
            "name": "LabelPerComponent",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "max_length": 64,
        }
    )
    supporting_representation: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "SupportingRepresentation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    local_crs: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "LocalCrs",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    time_or_interval_series: Optional[TimeOrIntervalSeries] = field(
        default=None,
        metadata={
            "name": "TimeOrIntervalSeries",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
