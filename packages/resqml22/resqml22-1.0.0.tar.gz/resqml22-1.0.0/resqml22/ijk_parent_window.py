from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.abstract_integer_array import AbstractIntegerArray
from resqml22.abstract_parent_window import AbstractParentWindow
from resqml22.data_object_reference import DataObjectReference
from resqml22.regrid import Regrid

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class IjkParentWindow(AbstractParentWindow):
    """
    Parent window for any IJK grid.

    :ivar omit_parent_cells: List of parent cells that are to be
        retained at their original resolution and are not to be included
        within a local grid. The "omit" allows non-rectangular local
        grids to be specified. 0-based indexing follows NI x NJ x NK
        relative to the parent window cell count—not to the parent grid.
    :ivar jregrid:
    :ivar parent_ijk_grid_representation:
    :ivar kregrid:
    :ivar iregrid:
    """
    omit_parent_cells: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "OmitParentCells",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    jregrid: Optional[Regrid] = field(
        default=None,
        metadata={
            "name": "JRegrid",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    parent_ijk_grid_representation: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "ParentIjkGridRepresentation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
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
    iregrid: Optional[Regrid] = field(
        default=None,
        metadata={
            "name": "IRegrid",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
