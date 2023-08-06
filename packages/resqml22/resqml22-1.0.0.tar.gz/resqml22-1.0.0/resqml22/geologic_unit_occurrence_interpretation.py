from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from resqml22.abstract_geologic_unit_organization_interpretation import AbstractGeologicUnitOrganizationInterpretation
from resqml22.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class GeologicUnitOccurrenceInterpretation(AbstractGeologicUnitOrganizationInterpretation):
    """A local Interpretation—it could be along a well, on a 2D map, or on a 2D section or on a part of the global volume of an earth model—of a succession of rock feature elements.
    The stratigraphic column rank interpretation composing a stratigraphic occurrence can be ordered by the criteria listed in OrderingCriteria.
    Note: When the chosen ordering criterion is not age but measured depth along a well trajectory, the semantics of the name of this class could be inconsistent semantics. In this case:
    - When faults are present, the observed succession may show repetition of a stratigraphic succession composed of a series of units each younger than the one below it.
    - This succession should not be called a stratigraphic occurrence because it is not stratigraphic (because the adjective ‘stratigraphic’ applies to a succession of units ordered according to their relative ages).
    A more general term for designating a succession of geological units encountered in drilling would be "Geologic Occurrence". So we may consider that the term "stratigraphic cccurrence interpretation" should be understood as "geologic occurrence interpretation"."""
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    geologic_unit: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "GeologicUnit",
            "type": "Element",
        }
    )
    is_occurrence_of: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "IsOccurrenceOf",
            "type": "Element",
        }
    )
