from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from resqml22.abstract_property import AbstractProperty
from resqml22.abstract_value_array import AbstractValueArray
from resqml22.property_kind_facet import PropertyKindFacet

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class AbstractValuesProperty(AbstractProperty):
    """Base class for property values.

    Each derived element provides specific property values, including
    point property in support of geometries.

    :ivar values_for_patch: If the rep has no explicit patch, use only 1
        ValuesForPatch.  If the rep has &gt; 1 explicit patch, use as
        many ValuesforPatch as patches of the rep. The ordering of
        ValuesForPatch matches the ordering of the patches in the xml
        document of the representation.
    :ivar facet:
    """
    values_for_patch: List[AbstractValueArray] = field(
        default_factory=list,
        metadata={
            "name": "ValuesForPatch",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "min_occurs": 1,
        }
    )
    facet: List[PropertyKindFacet] = field(
        default_factory=list,
        metadata={
            "name": "Facet",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
