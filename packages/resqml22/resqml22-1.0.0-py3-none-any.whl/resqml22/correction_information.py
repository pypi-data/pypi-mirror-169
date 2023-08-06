from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class CorrectionInformation:
    """
    Occurs only if a correction has been applied on the survey wellbore.

    :ivar correction_average_velocity: The UOM is composed by: UOM of
        the LocalDepth3dCrs of the associated wellbore frame trajectory
        / UOM of the associated LocalTime3dCrs. If not used, enter zero.
    :ivar correction_time_shift: The UOM is the one specified in the
        LocalTime3dCrs. If not used, enter zero.
    """
    correction_average_velocity: float = field(
        default=0.0,
        metadata={
            "name": "CorrectionAverageVelocity",
            "type": "Attribute",
        }
    )
    correction_time_shift: float = field(
        default=0.0,
        metadata={
            "name": "CorrectionTimeShift",
            "type": "Attribute",
        }
    )
