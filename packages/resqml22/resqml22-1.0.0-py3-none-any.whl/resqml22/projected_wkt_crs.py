from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.abstract_projected_crs import AbstractProjectedCrs

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class ProjectedWktCrs(AbstractProjectedCrs):
    """
    ISO 19162-compliant well-known text for the projected CRS.

    :ivar well_known_text: ISO 19162 compliant well known text of the
        CRS
    """
    well_known_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "WellKnownText",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
