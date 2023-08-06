from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.abstract_parent_window import AbstractParentWindow
from resqml22.abstract_representation import AbstractRepresentation
from resqml22.cell_fluid_phase_units import CellFluidPhaseUnits
from resqml22.interval_stratigraphic_units import IntervalStratigraphicUnits

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class AbstractGridRepresentation(AbstractRepresentation):
    """
    Abstract class for all grid representations.
    """
    cell_fluid_phase_units: Optional[CellFluidPhaseUnits] = field(
        default=None,
        metadata={
            "name": "CellFluidPhaseUnits",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    parent_window: Optional[AbstractParentWindow] = field(
        default=None,
        metadata={
            "name": "ParentWindow",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    interval_stratigraphic_units: Optional[IntervalStratigraphicUnits] = field(
        default=None,
        metadata={
            "name": "IntervalStratigraphicUnits",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
