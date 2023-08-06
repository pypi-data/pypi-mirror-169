from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from resqml22.boundary_feature_interpretation import BoundaryFeatureInterpretation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class GeobodyBoundaryInterpretation(BoundaryFeatureInterpretation):
    """
    Contains the data describing an opinion about the characterization of a
    geobody BoundaryFeature, and it includes the attribute boundary relation.

    :ivar boundary_relation: Characterizes the stratigraphic
        relationships of a horizon with the stratigraphic units that its
        bounds.
    :ivar is_conformable_above: Optional Boolean flag to indicate that
        the geobody boundary interpretation is conformable above.
    :ivar is_conformable_below: Optional Boolean flag to indicate that
        the geobody boundary interpretation is conformable below.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    boundary_relation: List[str] = field(
        default_factory=list,
        metadata={
            "name": "BoundaryRelation",
            "type": "Element",
        }
    )
    is_conformable_above: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsConformableAbove",
            "type": "Element",
        }
    )
    is_conformable_below: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsConformableBelow",
            "type": "Element",
        }
    )
