from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from resqml22.abstract_feature_interpretation import AbstractFeatureInterpretation
from resqml22.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class EarthModelInterpretation(AbstractFeatureInterpretation):
    """An earth model interpretation has the specific role of gathering at
    most:

    - one StratigraphicOrganizationInterpretation
    - One or several StructuralOrganizationInterpretations
    - One or several RockFluidOrganizationInterpretations
    BUSINESS RULE: An earth model Interpretation interprets only a model feature.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    stratigraphic_occurrences: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "StratigraphicOccurrences",
            "type": "Element",
        }
    )
    wellbore_interpretation_set: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "WellboreInterpretationSet",
            "type": "Element",
        }
    )
    stratigraphic_column: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "StratigraphicColumn",
            "type": "Element",
        }
    )
    structure: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "Structure",
            "type": "Element",
        }
    )
    fluid: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "Fluid",
            "type": "Element",
        }
    )
