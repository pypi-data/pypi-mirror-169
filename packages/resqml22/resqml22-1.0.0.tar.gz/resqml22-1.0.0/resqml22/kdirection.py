from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


class Kdirection(Enum):
    """Enumeration used to specify if the direction of the coordinate lines is
    uniquely defined for a grid.

    If not uniquely defined, e.g., for over-turned reservoirs, then
    indicate that the K direction is not monotonic.

    :cvar DOWN: K is increasing with depth, dot(tangent,gradDepth)&gt;0.
    :cvar UP: K is increasing with elevation,
        dot(tangent,gradDepth)&lt;0.
    :cvar NOT_MONOTONIC: K is not monotonic with elevation, e.g., for
        over-turned structures.
    """
    DOWN = "down"
    UP = "up"
    NOT_MONOTONIC = "not monotonic"
