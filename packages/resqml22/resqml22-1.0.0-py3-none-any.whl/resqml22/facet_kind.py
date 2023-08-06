from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class FacetKind(Enum):
    """Enumerations of the type of qualifier that applies to a property type to
    provide additional context about the nature of the property.

    For example, may include conditions, direction, qualifiers, or
    statistics. Facets are used in RESQML to provide qualifiers to
    existing property types, which minimizes the need to create
    specialized property types.

    :cvar CONDITIONS: Indicates condition of how the property was
        acquired, e.g., distinguishing surface condition of a fluid
        compared to reservoir conditions.
    :cvar SIDE: Indicates on which side of a surface the property
        applies, for example, it can indicate plus or minus.
    :cvar DIRECTION: Indicates that the property is directional. Common
        values are X, Y, or Z for vectors; I, J, or K for properties on
        a grid; or tensorial coordinates, e.g., XX or IJ. For example,
        vertical permeability vs. horizontal permeability.
    :cvar NETGROSS: Indicates that the property is of kind net or gross,
        i.e., indicates that the spatial support of a property is
        averaged only over the net rock or all of the rock. rock or all
        of the rock.
    :cvar QUALIFIER: Used to capture any other context not covered by
        the other facet types listed here.
    :cvar STATISTICS: Indicates values such as minimum, maximum,
        average, etc.
    :cvar WHAT: Indicates the element that is measured, for example, the
        concentration of a mineral.
    """
    CONDITIONS = "conditions"
    SIDE = "side"
    DIRECTION = "direction"
    NETGROSS = "netgross"
    QUALIFIER = "qualifier"
    STATISTICS = "statistics"
    WHAT = "what"
