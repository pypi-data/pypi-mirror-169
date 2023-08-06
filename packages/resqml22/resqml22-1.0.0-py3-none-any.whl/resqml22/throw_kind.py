from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


class ThrowKind(Enum):
    """
    Enumeration that characterizes the type of discontinuity corresponding to a
    fault.

    :cvar REVERSE:
    :cvar STRIKE_SLIP:
    :cvar NORMAL:
    :cvar THRUST:
    :cvar SCISSOR:
    :cvar VARIABLE: Used when a throw has different behaviors during its
        lifetime.
    """
    REVERSE = "reverse"
    STRIKE_SLIP = "strike-slip"
    NORMAL = "normal"
    THRUST = "thrust"
    SCISSOR = "scissor"
    VARIABLE = "variable"
