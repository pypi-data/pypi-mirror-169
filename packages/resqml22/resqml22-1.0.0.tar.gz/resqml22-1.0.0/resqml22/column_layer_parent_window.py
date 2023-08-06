from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.abstract_integer_array import AbstractIntegerArray
from resqml22.abstract_parent_window import AbstractParentWindow
from resqml22.data_object_reference import DataObjectReference
from resqml22.regrid import Regrid

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ColumnLayerParentWindow(AbstractParentWindow):
    """
    Parent window for any column-layer grid indexed as if it were an
    unstructured column layer grid, i.e., IJ columns are replaced by a column
    index.

    :ivar column_indices: Column indices that list the columns in the
        parent window. BUSINESS RULE: The ratio of fine to coarse column
        counts must be an integer for each coarse column.
    :ivar omit_parent_cells: List of parent cells that are to be
        retained at their original resolution and are not to be included
        within a local grid. The "omit" allows non-rectangular local
        grids to be specified. 0-based indexing follows #Columns x
        #Layers relative to the parent window cell count, not to the
        parent grid.
    :ivar kregrid:
    :ivar parent_column_layer_grid_representation:
    """
    column_indices: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "ColumnIndices",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    omit_parent_cells: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "OmitParentCells",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    kregrid: Optional[Regrid] = field(
        default=None,
        metadata={
            "name": "KRegrid",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    parent_column_layer_grid_representation: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "ParentColumnLayerGridRepresentation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
