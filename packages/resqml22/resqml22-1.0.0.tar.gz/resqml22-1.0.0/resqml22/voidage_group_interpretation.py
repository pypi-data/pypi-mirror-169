from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from resqml22.abstract_organization_interpretation import AbstractOrganizationInterpretation
from resqml22.data_object_reference import DataObjectReference
from resqml22.reservoir_compartment_interpretation import ReservoirCompartmentInterpretation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class VoidageGroupInterpretation(AbstractOrganizationInterpretation):
    """A group of ReservoirSegments which are hydraulically connected and are
    generally developed as a single reservoir.

    Membership in this organization can change over time (geologic and
    over the life of a field or interpretation activity) and is an
    interpretation.
    """
    stratigraphy: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Stratigraphy",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    fluids: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Fluids",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    compartments: List[ReservoirCompartmentInterpretation] = field(
        default_factory=list,
        metadata={
            "name": "Compartments",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
