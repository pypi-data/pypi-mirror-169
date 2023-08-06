from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.abstract_boolean_array import AbstractBooleanArray
from resqml22.abstract_integer_array import AbstractIntegerArray
from resqml22.jagged_array import JaggedArray

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class TruncationCellPatch:
    """Truncation definitions for the truncated and split cells.

    BUSINESS RULE: Patch Index must be positive because a patch index of
    0 refers to the fundamental column-layer coordinate line nodes and
    cells.

    :ivar local_faces_per_cell: Local cell face index for those faces
        that are retained from the parent cell in the definition of the
        truncation cell. The use of a local cell-face index, e.g., 0...5
        for an IJK cell, can be used even if the face indices have not
        been defined.
    :ivar nodes_per_truncation_face: Definition of the truncation faces
        is in terms of an ordered list of nodes. Node indexing is
        EXTENDED, i.e., is based on the list of untruncated grid nodes
        (always first) plus the split nodes (if any) and the truncation
        face nodes. Relative order of split nodes and truncation face
        nodes is set by the pillar indices.
    :ivar parent_cell_indices: Parent cell index for each of the
        truncation cells. BUSINESS RULE: Size must match
        truncationCellCount
    :ivar truncation_cell_count: Number of polyhedral cells created by
        truncation. Must be positive. Note: Parent cells are replaced.
    :ivar truncation_cell_face_is_right_handed: Boolean mask used to
        indicate which truncation cell faces have an outwardly directed
        normal, following a right hand rule. Data size and order follows
        the truncationFacesPerCell list-of-lists.
    :ivar truncation_face_count: Number of additional faces required for
        the split and truncation construction. The construction does not
        modify existing face definitions, but instead uses these new
        faces to redefine the truncated cell geometry. Must be positive.
        These faces are added to the enumeration of faces for the grid
    :ivar truncation_faces_per_cell: Truncation face index for the
        additional cell faces that are required to complete the
        definition of the truncation cell. The resulting local cell face
        index follows the local faces-per-cell list, followed by the
        truncation faces in the order within the list-of-lists
        constructions.
    :ivar truncation_node_count: Number of additional nodes required for
        the truncation construction. Must be positive. Uses a separate
        enumeration and does not increase the number of nodes, except as
        noted below.
    """
    local_faces_per_cell: Optional[JaggedArray] = field(
        default=None,
        metadata={
            "name": "LocalFacesPerCell",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    nodes_per_truncation_face: Optional[JaggedArray] = field(
        default=None,
        metadata={
            "name": "NodesPerTruncationFace",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    parent_cell_indices: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "ParentCellIndices",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    truncation_cell_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "TruncationCellCount",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
            "min_inclusive": 1,
        }
    )
    truncation_cell_face_is_right_handed: Optional[AbstractBooleanArray] = field(
        default=None,
        metadata={
            "name": "TruncationCellFaceIsRightHanded",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    truncation_face_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "TruncationFaceCount",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
            "min_inclusive": 1,
        }
    )
    truncation_faces_per_cell: Optional[JaggedArray] = field(
        default=None,
        metadata={
            "name": "TruncationFacesPerCell",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    truncation_node_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "TruncationNodeCount",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
            "min_inclusive": 1,
        }
    )
