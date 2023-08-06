from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.deposition_mode import DepositionMode
from resqml22.geologic_unit_interpretation import GeologicUnitInterpretation
from resqml22.length_measure import LengthMeasure
from resqml22.stratigraphic_role import StratigraphicRole

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class StratigraphicUnitInterpretation(GeologicUnitInterpretation):
    """A volume of rock of identifiable origin and relative age range that is
    defined by the distinctive and dominant, easily mapped and recognizable
    features that characterize it (petrographic, lithologic, paleontologic,
    paleomagnetic or chemical features).

    Some stratigraphic units (chronostratigraphic units) have a
    GeneticBoundaryBasedTimeInterval (between its ChronoTop and
    ChronoBottom) defined by a BoundaryFeatureInterpretation. A
    stratigraphic unit has no direct link to its physical top and bottom
    limits. These physical limits are only defined as contacts between
    StratigraphicUnitInterpretations defined within a
    StratigraphicOrganizationInterpretation.

    :ivar deposition_mode: BUSINESS RULE: The deposition mode for a
        geological unit MUST be consistent with the boundary relations
        of a genetic boundary. If it is not, then the boundary relation
        declaration is retained.
    :ivar max_thickness:
    :ivar min_thickness:
    :ivar stratigraphic_role:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    deposition_mode: Optional[DepositionMode] = field(
        default=None,
        metadata={
            "name": "DepositionMode",
            "type": "Element",
        }
    )
    max_thickness: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "MaxThickness",
            "type": "Element",
        }
    )
    min_thickness: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "MinThickness",
            "type": "Element",
        }
    )
    stratigraphic_role: Optional[StratigraphicRole] = field(
        default=None,
        metadata={
            "name": "StratigraphicRole",
            "type": "Element",
        }
    )
