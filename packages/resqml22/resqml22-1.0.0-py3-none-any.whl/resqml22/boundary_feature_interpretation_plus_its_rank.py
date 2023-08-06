from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class BoundaryFeatureInterpretationPlusItsRank:
    """Element that lets you index and order feature interpretations which must
    be boundaries (horizon, faults and frontiers) or boundary sets (fault
    network).

    For possible ordering criteria, see OrderingCriteria. BUSINESS RULE:
    Only BoundaryFeatureInterpretation and FeatureInterpretationSet
    having faults as homogeneous type must be used to build a
    StructuralOrganizationInterpretation.

    :ivar stratigraphic_rank: The first rank on which you find the
        boundary or the interpretation set of boundaries.
    :ivar boundary_feature_interpretation:
    :ivar feature_interpretation_set:
    """
    stratigraphic_rank: Optional[int] = field(
        default=None,
        metadata={
            "name": "StratigraphicRank",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "min_inclusive": 0,
        }
    )
    boundary_feature_interpretation: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "BoundaryFeatureInterpretation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    feature_interpretation_set: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "FeatureInterpretationSet",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
