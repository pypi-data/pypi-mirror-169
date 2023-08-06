from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


class EdgePattern(Enum):
    """
    The graphical patterns that an edge can support.

    :cvar DASHED: The edge will display as a dashed (succession of
        dashes) line.
    :cvar DOTTED: The edge will display as a dotted (succession of dots)
        line.
    :cvar SOLID: The edge will display as a single line.
    :cvar WAVY: The edge will display as a wavy line.
    """
    DASHED = "dashed"
    DOTTED = "dotted"
    SOLID = "solid"
    WAVY = "wavy"
