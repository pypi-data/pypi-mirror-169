from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.abstract_projected_crs import AbstractProjectedCrs

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class ProjectedUnknownCrs(AbstractProjectedCrs):
    """This class is used in a case where the coordinate reference system is
    either unknown or is intentionally not being transferred.

    In this case, the uom and AxisOrder need to be provided on the
    ProjectedCrs class.
    """
    unknown: Optional[str] = field(
        default=None,
        metadata={
            "name": "Unknown",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
            "max_length": 2000,
        }
    )
