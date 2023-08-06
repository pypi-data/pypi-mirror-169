from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.abstract_point3d_array import AbstractPoint3DArray
from resqml22.data_object_reference import DataObjectReference
from resqml22.integer_lattice_array import IntegerLatticeArray

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class Point3DFromRepresentationLatticeArray(AbstractPoint3DArray):
    """A lattice array of points extracted from an existing representation.

    BUSINESS RULE: The supporting representation must have nodes as
    indexable elements.

    :ivar node_indices_on_supporting_representation: The node indices of
        the selected nodes in the supporting representation. The index
        selection is regularly incremented from one node to the next
        node. BUSINESS RULE: The node indices must be consistent with
        the size of supporting representation.
    :ivar supporting_representation:
    """
    class Meta:
        name = "Point3dFromRepresentationLatticeArray"

    node_indices_on_supporting_representation: Optional[IntegerLatticeArray] = field(
        default=None,
        metadata={
            "name": "NodeIndicesOnSupportingRepresentation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
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
