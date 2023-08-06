from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.interval_grid_cells import IntervalGridCells
from resqml22.wellbore_frame_representation import WellboreFrameRepresentation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class BlockedWellboreRepresentation(WellboreFrameRepresentation):
    """
    The information that allows you to locate, on one or several grids
    (existing or planned), the intersection of volume (cells) and surface
    (faces) elements with a wellbore trajectory (existing or planned).
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    interval_grid_cells: Optional[IntervalGridCells] = field(
        default=None,
        metadata={
            "name": "IntervalGridCells",
            "type": "Element",
            "required": True,
        }
    )
