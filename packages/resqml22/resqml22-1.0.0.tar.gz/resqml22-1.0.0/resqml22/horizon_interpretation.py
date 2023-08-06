from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional, Union
from resqml22.boundary_feature_interpretation import BoundaryFeatureInterpretation
from resqml22.sequence_stratigraphy_surface_kind import SequenceStratigraphySurfaceKind
from resqml22.stratigraphic_role import StratigraphicRole

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class HorizonInterpretation(BoundaryFeatureInterpretation):
    """An interpretation of a horizon, which optionally provides stratigraphic information on BoundaryRelation, HorizonStratigraphicRole, SequenceStratigraphysurface
    .

    :ivar is_conformable_above: Optional Boolean flag to indicate that
        the horizon interpretation is conformable above.
    :ivar is_conformable_below: Optional Boolean flag to indicate that
        the horizon interpretation is conformable below.
    :ivar stratigraphic_role:
    :ivar sequence_stratigraphy_surface:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

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
    stratigraphic_role: List[StratigraphicRole] = field(
        default_factory=list,
        metadata={
            "name": "StratigraphicRole",
            "type": "Element",
        }
    )
    sequence_stratigraphy_surface: Optional[Union[SequenceStratigraphySurfaceKind, str]] = field(
        default=None,
        metadata={
            "name": "SequenceStratigraphySurface",
            "type": "Element",
            "pattern": r".*:.*",
        }
    )
