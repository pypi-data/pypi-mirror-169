from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from resqml22.abstract_integer_array import AbstractIntegerArray
from resqml22.abstract_representation import AbstractRepresentation
from resqml22.connection_interpretations import ConnectionInterpretations
from resqml22.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class GridConnectionSetRepresentation(AbstractRepresentation):
    """Representation that consists of a list of connections between grid
    cells, potentially on different grids.

    Connections are in the form of
    (Grid,Cell,Face)1&lt;=&gt;(Grid,Cell,Face)2 and are stored as three
    integer pair arrays corresponding to these six elements. Grid
    connection sets are the preferred means of representing faults on a
    grid. The use of cell-face-pairs is more complete than single cell-
    faces, which are missing a corresponding cell face entry, and only
    provide an incomplete representation of the topology of a fault.
    Unlike what is sometimes the case in reservoir simulation software,
    RESQML does not distinguish between standard and non-standard
    connections. Within RESQML, if a grid connection corresponds to a
    "nearest neighbor" as defined by the cell indices, then it is never
    additive to the implicit nearest neighbor connection. BUSINESS RULE:
    A single cell-face-pair should not appear within more than a single
    grid connection set. This rule is designed to simplify the
    interpretation of properties assigned to multiple grid connection
    sets, which might otherwise have the same property defined more than
    once on a single connection, with no clear means of resolving the
    multiple values.

    :ivar count: count of connections. Must be positive.
    :ivar cell_index_pairs: 2 x #Connections array of cell indices for
        (Cell1,Cell2) for each connection.
    :ivar grid_index_pairs: 2 x #Connections array of grid indices for
        (Cell1,Cell2) for each connection. The grid indices are obtained
        from the grid index pairs. If only a single grid is referenced
        from the grid index, then this array need not be used. BUSINESS
        RULE: If more than one grid index pair is referenced, then this
        array should appear.
    :ivar local_face_per_cell_index_pairs: Optional 2 x #Connections
        array of local face-per-cell indices for (Cell1,Cell2) for each
        connection. Local face-per-cell indices are used because global
        face indices need not have been defined. If no face-per-cell
        definition occurs as part of the grid representation, e.g., for
        a block-centered grid, then this array need not appear.
    :ivar connection_interpretations:
    :ivar grid:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    count: Optional[int] = field(
        default=None,
        metadata={
            "name": "Count",
            "type": "Element",
            "required": True,
            "min_inclusive": 1,
        }
    )
    cell_index_pairs: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "CellIndexPairs",
            "type": "Element",
            "required": True,
        }
    )
    grid_index_pairs: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "GridIndexPairs",
            "type": "Element",
        }
    )
    local_face_per_cell_index_pairs: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "LocalFacePerCellIndexPairs",
            "type": "Element",
        }
    )
    connection_interpretations: Optional[ConnectionInterpretations] = field(
        default=None,
        metadata={
            "name": "ConnectionInterpretations",
            "type": "Element",
        }
    )
    grid: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "Grid",
            "type": "Element",
            "min_occurs": 1,
        }
    )
