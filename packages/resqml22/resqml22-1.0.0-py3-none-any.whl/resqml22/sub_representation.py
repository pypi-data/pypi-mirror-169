from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from resqml22.abstract_representation import AbstractRepresentation
from resqml22.additional_grid_topology import AdditionalGridTopology
from resqml22.indexable_element import IndexableElement
from resqml22.sub_representation_patch import SubRepresentationPatch

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class SubRepresentation(AbstractRepresentation):
    """An ordered list of indexable elements and/or indexable element pairs of
    an existing representation.

    Because the representation concepts of topology, geometry, and
    property values are separate in RESQML, it is now possible to select
    a range of nodes, edges, faces, or volumes (cell) indices from the
    topological support of an existing representation to define a sub-
    representation. A sub-representation may describe a different
    feature interpretation using the same geometry or property as the
    "parent" representation. In this case, the only information
    exchanged is a set of potentially non-consecutive indices of the
    topological support of the representation. Optional additional grid
    topology is available for grid representations.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    indexable_element: Optional[IndexableElement] = field(
        default=None,
        metadata={
            "name": "IndexableElement",
            "type": "Element",
            "required": True,
        }
    )
    additional_grid_topology: Optional[AdditionalGridTopology] = field(
        default=None,
        metadata={
            "name": "AdditionalGridTopology",
            "type": "Element",
        }
    )
    sub_representation_patch: List[SubRepresentationPatch] = field(
        default_factory=list,
        metadata={
            "name": "SubRepresentationPatch",
            "type": "Element",
            "min_occurs": 1,
        }
    )
