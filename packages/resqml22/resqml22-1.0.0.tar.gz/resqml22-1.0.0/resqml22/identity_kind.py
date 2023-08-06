from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


class IdentityKind(Enum):
    """
    Enumeration of the identity kinds for the element identities
    (ElementIdentity).

    :cvar COLLOCATION: A set of (sub)representations is collocated if
        there is bijection between the simple elements of all of the
        participating (sub)representations. This definition implies
        there is the same number of simple elements. NOTE: The geometric
        location of each set of simple elements mapped through the
        bijection is intended to be identical even if the numeric values
        of the associated geometries differ, i.e., due to loss of
        spatial resolution.
    :cvar PREVIOUS_COLLOCATION: The participating (sub)representations
        were collocated at some time in the geologic past—but not
        necessarily in the present day earth model.
    :cvar EQUIVALENCE: A set of (sub)representations is equivalent if
        there is a map giving an association between some of the simple
        topological elements of the participating (sub)representations.
    :cvar PREVIOUS_EQUIVALENCE: The participating (sub)representations
        were equivalent at some time in the geologic past—but not
        necessarily in the present day earth model.
    """
    COLLOCATION = "collocation"
    PREVIOUS_COLLOCATION = "previous collocation"
    EQUIVALENCE = "equivalence"
    PREVIOUS_EQUIVALENCE = "previous equivalence"
