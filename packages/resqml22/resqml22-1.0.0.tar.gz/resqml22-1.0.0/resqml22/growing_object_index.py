from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from resqml22.data_index_kind import DataIndexKind
from resqml22.data_object_reference import DataObjectReference
from resqml22.index_direction import IndexDirection
from resqml22.legacy_unit_of_measure import LegacyUnitOfMeasure
from resqml22.unit_of_measure import UnitOfMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class GrowingObjectIndex:
    """Common information about the index for a growing object.

    IMMUTABLE. Set on object creation and MUST NOT change thereafter.
    Customer provided changes after creation are an error. None of the
    sub-elements can be changed.

    :ivar index_kind: The kind of index (date time, measured depth,
        etc.). IMMUTABLE. Set on object creation and MUST NOT change
        thereafter. Customer provided changes after creation are an
        error.
    :ivar index_property_kind: An optional value pointing to a
        PropertyKind. Energistics provides a list of standard property
        kinds that represent the basis for the commonly used properties
        in the E&amp;P subsurface workflow. This PropertyKind
        enumeration is in the external PropertyKindDictionary XML file
        in the Common ancillary folder. IMMUTABLE. Set on object
        creation and MUST NOT change thereafter. Customer provided
        changes after creation are an error.
    :ivar uom: The unit of measure of the index. Must be one of the
        units allowed for the specified IndexKind (e.g., time or depth).
        IMMUTABLE. Set on object creation and MUST NOT change
        thereafter. Customer provided changes after creation are an
        error.
    :ivar direction: The direction of the index, either increasing or
        decreasing. Index direction may not change within the life of a
        growing object. IMMUTABLE. Set on object creation and MUST NOT
        change thereafter. Customer provided changes after creation are
        an error.
    :ivar datum: For depth indexes, this is a pointer to a reference
        point defining the datum to which all of the index values are
        referenced. IMMUTABLE. Set on object creation and MUST NOT
        change thereafter. Customer provided changes after creation are
        an error.
    """
    index_kind: Optional[DataIndexKind] = field(
        default=None,
        metadata={
            "name": "IndexKind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    index_property_kind: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "IndexPropertyKind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
        }
    )
    uom: Optional[Union[LegacyUnitOfMeasure, UnitOfMeasure, str]] = field(
        default=None,
        metadata={
            "name": "Uom",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
            "pattern": r".*:.*",
        }
    )
    direction: Optional[IndexDirection] = field(
        default=None,
        metadata={
            "name": "Direction",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    datum: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Datum",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
        }
    )
