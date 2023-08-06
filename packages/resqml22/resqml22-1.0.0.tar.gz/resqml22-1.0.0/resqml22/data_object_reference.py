from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from resqml22.extension_name_value import ExtensionNameValue

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class DataObjectReference:
    """
    A pointer to another Energistics data object.

    :ivar uuid: Universally unique identifier (UUID) of the referenced
        data object. For rules and guidelines about the format of UUIDs
        with the current version of Energistics standards, see the
        Energistics Identifier Specification v5.0.
    :ivar object_version: Indicates the version of the data object that
        is referenced. This must be identical to the objectVersion
        attribute that is inherited from AbstractObject. If this element
        is empty, then the latest version of the data object is assumed.
    :ivar qualified_type: The qualified type of the referenced data
        object. It is the semantic equivalent of a qualifiedEntityType
        in OData (which is the DataObjectType used in the Energistics
        Transfer Protocol (ETP)). For more information, see the
        Energistics Identifier Specification v5.0. The QualifiedType is
        composed of: - The Energistics domain standard or Energistics
        common (designated by eml) and version where the data object
        type is defined. - The data object type name as defined by its
        schema. Examples: - witsml20.Well -
        resqml20.UnstructuredGridRepresentation - prodml20.ProductVolume
        - eml21.DataAssuranceRecord
    :ivar title: The title of the referenced data object. It should be
        the value in the Title attribute of the Citation element in
        AbstractObject. It is used as a hint for human readers; it is
        not enforced to match the Title of the referenced data object.
    :ivar energistics_uri: The canonical URI of a referenced data
        object. This element is intended for use with the Energistics
        Transfer Protocol (ETP) . Do not use this element to store the
        path and file names of an external data object object.
        Optionally use one or more LocatorUrl elements to provide hints
        on how to resolve the URI into a data object.
    :ivar locator_url: An optional location to help in finding the
        correct referenced data object.
    :ivar extension_name_value: A standard Energistics extension
        mechanism used to add custom data in the format of name:value
        pairs.
    """
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "name": "Uuid",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    object_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "ObjectVersion",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "max_length": 64,
        }
    )
    qualified_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "QualifiedType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
            "max_length": 256,
            "pattern": r"(witsml|resqml|prodml|eml|custom)[1-9]\d\.\w+",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "name": "Title",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
            "max_length": 2000,
        }
    )
    energistics_uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "EnergisticsUri",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
        }
    )
    locator_url: List[str] = field(
        default_factory=list,
        metadata={
            "name": "LocatorUrl",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
        }
    )
    extension_name_value: List[ExtensionNameValue] = field(
        default_factory=list,
        metadata={
            "name": "ExtensionNameValue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
        }
    )
