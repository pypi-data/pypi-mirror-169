from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


class ColumnShape(Enum):
    """Used to indicate that all columns are of a uniform topology, i.e., have
    the same number of faces per column.

    This information is supplied by the RESQML writer to indicate the
    complexity of the grid geometry, as an aide to the RESQML reader. If
    a specific column shape is not appropriate, then use polygonal.
    BUSINESS RULE: Should be consistent with the actual geometry of the
    grid.

    :cvar TRIANGULAR: All grid columns have 3 sides.
    :cvar QUADRILATERAL: All grid columns have 4 sides. Includes tartan
        and corner point grids.
    :cvar POLYGONAL: At least one grid column is a polygon, N&gt;4.
    """
    TRIANGULAR = "triangular"
    QUADRILATERAL = "quadrilateral"
    POLYGONAL = "polygonal"
