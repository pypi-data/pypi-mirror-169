from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.boundary_feature_interpretation import BoundaryFeatureInterpretation
from resqml22.fluid_contact import FluidContact

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class FluidBoundaryInterpretation(BoundaryFeatureInterpretation):
    """A boundary (usually a plane or a set of planes) separating two fluid
    phases, such as a gas-oil contact (GOC), a water-oil contact (WOC), a gas-
    oil contact (GOC), or others.

    For types, see FluidContact.

    :ivar fluid_contact: The kind of contact of this boundary.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    fluid_contact: Optional[FluidContact] = field(
        default=None,
        metadata={
            "name": "FluidContact",
            "type": "Element",
            "required": True,
        }
    )
