from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.marker_boundary import MarkerBoundary

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class StratigraphicIntervalBoundary(MarkerBoundary):
    """
    This represents a stratigraphic boundary between two intervals.

    :ivar contact_conformable_above: This is an optional boolean
        indicating that the relationship between the boundary and the
        unit above is conformable. It is typically used as a placeholder
        for the interpreter to put some information before the
        association with an organization is made.
    :ivar contact_conformable_below: This is an optional boolean
        indicating that the relationship between the boundary and the
        unit below is conformable. It is typically used as a placeholder
        for the interpreter to put some information before the
        association with an organization is made.
    """
    contact_conformable_above: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ContactConformableAbove",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    contact_conformable_below: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ContactConformableBelow",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
