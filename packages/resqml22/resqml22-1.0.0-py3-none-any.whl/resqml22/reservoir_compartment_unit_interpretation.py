from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from resqml22.data_object_reference import DataObjectReference
from resqml22.reservoir_compartment_interpretation import ReservoirCompartmentInterpretation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ReservoirCompartmentUnitInterpretation:
    """
    A geologic unit or formation located within a reservoir compartment.
    """
    fluid_units: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "FluidUnits",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "max_occurs": 3,
        }
    )
    reservoir_compartment: Optional[ReservoirCompartmentInterpretation] = field(
        default=None,
        metadata={
            "name": "ReservoirCompartment",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    geologic_unit_interpretation: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "GeologicUnitInterpretation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
