from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.abstract_horizontal_coordinates import AbstractHorizontalCoordinates
from resqml22.public_land_survey_system_location import PublicLandSurveySystemLocation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class PublicLandSurveySystemCoordinates(AbstractHorizontalCoordinates):
    """Coordinates given in the US Public Land Survey System (Jeffersonian
    surveying).

    The parameters in the PublicLandSurveySystem element form a local
    engineering coordinate reference system with coordinate1 and
    coordinate2 being the distances in feet from the edge lines of the
    defined section fraction. The order and direction of the coordinates
    are given in the AxisOrder element, which is validated via the
    AxisOrder2d enumeration.
    """
    public_land_survey_system: Optional[PublicLandSurveySystemLocation] = field(
        default=None,
        metadata={
            "name": "PublicLandSurveySystem",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
