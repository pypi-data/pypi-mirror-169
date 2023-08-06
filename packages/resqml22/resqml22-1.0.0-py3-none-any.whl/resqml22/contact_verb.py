from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


class ContactVerb(Enum):
    """
    Enumerations for the verbs that can be used to define the impact on the
    construction of the model of the geological event that created the binary
    contact.

    :cvar STOPS: Specifies that an interpretation stops/interrupts
        another interpretation. Used for tectonic boundary vs tectonic
        boundary but also genetic boundary vs genetic boundary (erosion
        case), frontier vs interpretation, etc.
    :cvar SPLITS: Specifies that the fault has opened a pair of fault
        lips in a horizon or separated a geologic unit into two parts.
    :cvar CROSSES: Specifies that a tectonic boundary interpretation
        crosses another tectonic boundary interpretation.
    """
    STOPS = "stops"
    SPLITS = "splits"
    CROSSES = "crosses"
