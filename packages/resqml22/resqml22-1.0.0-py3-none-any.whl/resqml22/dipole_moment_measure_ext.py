from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from resqml22.dipole_moment_uom import DipoleMomentUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class DipoleMomentMeasureExt:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[Union[DipoleMomentUom, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r".*:.*",
        }
    )
