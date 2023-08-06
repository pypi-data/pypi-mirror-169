from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.data_object_reference import DataObjectReference
from resqml22.jagged_array import JaggedArray

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class CellFluidPhaseUnits:
    """
    A mapping from cells to fluid phase unit interpretation to describe the
    initial hydrostatic fluid column.

    :ivar phase_unit_indices: Index of the phase unit kind within a
        given fluid phase organization for each cell. Follows the
        indexing defined by the PhaseUnit enumeration. When applied to
        the wellbore frame representation, the indexing is identical to
        the number of intervals. Since a single cell or interval may
        corresponds to several units, the mapping is done using a jagged
        array. Use null value if no fluid phase is present, e.g., within
        the seal. BUSINESS RULE: Array length is equal to the number of
        cells in the representation (grid, wellbore frame or blocked
        well).
    :ivar rock_fluid_organization_interpretation:
    """
    phase_unit_indices: Optional[JaggedArray] = field(
        default=None,
        metadata={
            "name": "PhaseUnitIndices",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    rock_fluid_organization_interpretation: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "RockFluidOrganizationInterpretation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
