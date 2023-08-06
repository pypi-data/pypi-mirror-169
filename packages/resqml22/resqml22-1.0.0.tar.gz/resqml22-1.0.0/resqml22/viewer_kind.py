from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


class ViewerKind(Enum):
    """
    Standardized kinds of viewers.

    :cvar VALUE_3D: A viewer where data objects are visualized in a 3D
        space.
    :cvar BASE_MAP: A viewer where data objects are visualized in 2D
        from above.
    :cvar SECTION: A viewer where data objects are laterally visualized
        in 2D.
    :cvar WELL_CORRELATION: A viewer where several well-related data
        objects (mostly channels and markers) are visualized against
        depth.
    """
    VALUE_3D = "3d"
    BASE_MAP = "base map"
    SECTION = "section"
    WELL_CORRELATION = "well correlation"
