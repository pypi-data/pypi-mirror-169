from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from resqml22.abstract_organization_interpretation import AbstractOrganizationInterpretation
from resqml22.boundary_feature_interpretation_plus_its_rank import BoundaryFeatureInterpretationPlusItsRank
from resqml22.data_object_reference import DataObjectReference
from resqml22.ordering_criteria import OrderingCriteria

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class StructuralOrganizationInterpretation(AbstractOrganizationInterpretation):
    """One of the main types of RESQML organizations, this class gathers
    boundary interpretations (e.g., horizons, faults and fault networks) plus
    frontier features and their relationships (contacts interpretations), which
    when taken together define the structure of a part of the earth.

    IMPLEMENTATION RULE: Two use cases are presented:
    1. If the relative age or apparent depth between faults and horizons is unknown, the writer must provide all individual faults within the UnorderedFaultCollection FeatureInterpretationSet.
    2. Else, the writer must provide individual faults and fault collections within the OrderedBoundaryFeatureInterpretation list.
    BUSINESS RULE: Two use cases are processed:
    1. If relative age or apparent depth between faults and horizons are unknown, the writer must provides all individual faults within the UnorderedFaultCollection FeatureInterpretationSet.
    2. Else, individual faults and fault collections are provided within the OrderedBoundaryFeatureInterpretation list.

    :ivar ascending_ordering_criteria:
    :ivar bottom_frontier: BUSINESS RULE: It either points to a
        CulturalFeature whose Kind is model frontier or to a
        BoundaryFeatureInterpretation if the frontier is actually a
        geologic surface
    :ivar top_frontier: BUSINESS RULE: It either points to a
        CulturalFeature whose Kind is model frontier or to a
        BoundaryFeatureInterpretation if the frontier is actually a
        geologic surface
    :ivar sides: BUSINESS RULE: It either points to a CulturalFeature
        whose Kind is model frontier or to a
        BoundaryFeatureInterpretation if the frontier is actually a
        geologic surface
    :ivar ordered_boundary_feature_interpretation:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    ascending_ordering_criteria: Optional[OrderingCriteria] = field(
        default=None,
        metadata={
            "name": "AscendingOrderingCriteria",
            "type": "Element",
            "required": True,
        }
    )
    bottom_frontier: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "BottomFrontier",
            "type": "Element",
        }
    )
    top_frontier: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "TopFrontier",
            "type": "Element",
        }
    )
    sides: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "Sides",
            "type": "Element",
        }
    )
    ordered_boundary_feature_interpretation: List[BoundaryFeatureInterpretationPlusItsRank] = field(
        default_factory=list,
        metadata={
            "name": "OrderedBoundaryFeatureInterpretation",
            "type": "Element",
        }
    )
