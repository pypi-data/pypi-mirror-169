from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.abstract_values_property import AbstractValuesProperty
from resqml22.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class DiscreteProperty(AbstractValuesProperty):
    """Contains discrete integer values; typically used to store any type of
    index.

    Statistics about values such as maximum and minimum can be found in
    the statistics of each ValueForPatch.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    category_lookup: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "CategoryLookup",
            "type": "Element",
        }
    )
