from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.geologic_unit_interpretation import GeologicUnitInterpretation
from resqml22.phase import Phase

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class RockFluidUnitInterpretation(GeologicUnitInterpretation):
    """
    A type of rock fluid feature-interpretation, this class identifies a rock
    fluid unit interpretation by its phase.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    phase: Optional[Phase] = field(
        default=None,
        metadata={
            "name": "Phase",
            "type": "Element",
        }
    )
