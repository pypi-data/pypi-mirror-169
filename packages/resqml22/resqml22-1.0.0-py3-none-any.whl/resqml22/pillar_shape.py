from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


class PillarShape(Enum):
    """Used to indicate that all pillars are of a uniform kind, i.e., may be
    represented using the same number of nodes per pillar.

    This information is supplied by the RESQML writer to indicate the
    complexity of the grid geometry, as an aide to the RESQML reader. If
    a combination of vertical and straight, then use straight. If a
    specific pillar shape is not appropriate, then use curved. BUSINESS
    RULE: Should be consistent with the actual geometry of the grid.

    :cvar VERTICAL: If represented by a parametric line, requires only a
        single control point per line.
    :cvar STRAIGHT: If represented by a parametric line, requires 2
        control points per line.
    :cvar CURVED: If represented by a parametric line, requires 3 or
        more control points per line.
    """
    VERTICAL = "vertical"
    STRAIGHT = "straight"
    CURVED = "curved"
