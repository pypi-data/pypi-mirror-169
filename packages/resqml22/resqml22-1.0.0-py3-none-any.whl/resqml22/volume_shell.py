from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.boolean_external_array import BooleanExternalArray
from resqml22.integer_external_array import IntegerExternalArray

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class VolumeShell:
    """The shell or envelope of a geologic unit.

    It is a collection of macro faces. Each macro face is defined by a
    triplet of values, each value being at the same index in the three
    arrays contained in this class.

    :ivar patch_indices_of_representation: Each index identifies the
        surface representation patch describing the macro face.
    :ivar representation_indices: Each index identifies the macro face
        surface representation by its index in the list of
        representations contained in the organization.
    :ivar side_is_plus: Each index identifies the side of the macro
        face.
    """
    patch_indices_of_representation: Optional[IntegerExternalArray] = field(
        default=None,
        metadata={
            "name": "PatchIndicesOfRepresentation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    representation_indices: Optional[IntegerExternalArray] = field(
        default=None,
        metadata={
            "name": "RepresentationIndices ",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    side_is_plus: Optional[BooleanExternalArray] = field(
        default=None,
        metadata={
            "name": "SideIsPlus",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
