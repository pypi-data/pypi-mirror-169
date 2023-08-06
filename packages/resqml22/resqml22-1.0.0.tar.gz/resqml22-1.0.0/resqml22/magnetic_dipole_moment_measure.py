from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.magnetic_dipole_moment_uom import MagneticDipoleMomentUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class MagneticDipoleMomentMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[MagneticDipoleMomentUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
