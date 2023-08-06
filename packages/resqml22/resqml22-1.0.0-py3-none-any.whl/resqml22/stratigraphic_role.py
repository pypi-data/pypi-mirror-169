from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


class StratigraphicRole(Enum):
    """Interpretation of the stratigraphic role of a picked horizon (chrono,
    litho or bio).

    Here the word "role" is a business term which doesn’t correspond to
    an entity dependent from an external property but simply
    characterizes a kind of horizon.
    """
    CHRONOSTRATIGRAPHIC = "chronostratigraphic"
    LITHOSTRATIGRAPHIC = "lithostratigraphic"
    BIOSTRATIGRAPHIC = "biostratigraphic"
    MAGNETOSTRATIGRAPHIC = "magnetostratigraphic"
    CHEMOSTRATIGRAPHIC = "chemostratigraphic"
    SEISMICSTRATIGRAPHIC = "seismicstratigraphic"
