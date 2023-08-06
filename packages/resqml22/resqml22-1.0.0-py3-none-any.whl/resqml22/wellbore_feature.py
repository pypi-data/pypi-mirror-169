from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.abstract_technical_feature import AbstractTechnicalFeature
from resqml22.witsml_well_wellbore import WitsmlWellWellbore

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class WellboreFeature(AbstractTechnicalFeature):
    """May refer to one of these:

    wellbore. A unique, oriented path from the bottom of a drilled
    borehole to the surface of the earth. The path must not overlap or
    cross itself. borehole. A hole excavated in the earth as a result of
    drilling or boring operations. The borehole may represent the hole
    of an entire wellbore (when no sidetracks are present), or a
    sidetrack extension. A borehole extends from an originating point
    (the surface location for the initial borehole or kickoff point for
    sidetracks) to a terminating (bottomhole) point. sidetrack. A
    borehole that originates in another borehole as opposed to
    originating at the surface.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    witsml_wellbore: Optional[WitsmlWellWellbore] = field(
        default=None,
        metadata={
            "name": "WitsmlWellbore",
            "type": "Element",
        }
    )
