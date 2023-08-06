from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.abstract_floating_point_array import AbstractFloatingPointArray
from resqml22.volume_uom import VolumeUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class OverlapVolume:
    """Optional parent-child cell overlap volume information.

    If not present, then the CellOverlap data-object lists the overlaps,
    but with no additional information.

    :ivar overlap_volumes: Parent-child cell volume overlap. BUSINESS
        RULE: Length of array must equal the cell overlap count.
    :ivar volume_uom: Units of measure for the overlapVolume.
    """
    overlap_volumes: Optional[AbstractFloatingPointArray] = field(
        default=None,
        metadata={
            "name": "OverlapVolumes",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    volume_uom: Optional[VolumeUom] = field(
        default=None,
        metadata={
            "name": "VolumeUom",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
