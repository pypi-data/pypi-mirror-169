from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from resqml22.abstract_values_property import AbstractValuesProperty
from resqml22.data_object_reference import DataObjectReference
from resqml22.legacy_unit_of_measure import LegacyUnitOfMeasure
from resqml22.unit_of_measure import UnitOfMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ContinuousProperty(AbstractValuesProperty):
    """Most common type of property used for storing rock or fluid attributes;
    all are represented as doubles.

    Statistics about values such as maximum and minimum can be found in
    the statistics of each ValueForPatch. BUSINESS RULE: It also
    contains a unit of measure, which can be different from the unit of
    measure of its property type, but it must be convertible into this
    unit.

    :ivar uom: Unit of measure for the property.
    :ivar custom_unit_dictionary:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    uom: Optional[Union[LegacyUnitOfMeasure, UnitOfMeasure, str]] = field(
        default=None,
        metadata={
            "name": "Uom",
            "type": "Element",
            "required": True,
            "pattern": r".*:.*",
        }
    )
    custom_unit_dictionary: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "CustomUnitDictionary",
            "type": "Element",
        }
    )
