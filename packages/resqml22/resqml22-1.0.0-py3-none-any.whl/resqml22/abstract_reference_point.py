from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from resqml22.abstract_object import AbstractObject
from resqml22.osdureference_point_integration import OsdureferencePointIntegration
from resqml22.reference_point_kind import ReferencePointKind
from resqml22.vector import Vector

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class AbstractReferencePoint(AbstractObject):
    """A reference point is used as a new origin for some coordinates.

    It is not a CRS. Indeed, it does not redefine axis, uom, etc... it
    just defines the origin of some axis.
    """
    kind: Optional[Union[ReferencePointKind, str]] = field(
        default=None,
        metadata={
            "name": "Kind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "pattern": r".*:.*",
        }
    )
    osdureference_point_integration: Optional[OsdureferencePointIntegration] = field(
        default=None,
        metadata={
            "name": "OSDUReferencePointIntegration",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
        }
    )
    uncertainty_vector_at_one_sigma: Optional[Vector] = field(
        default=None,
        metadata={
            "name": "UncertaintyVectorAtOneSigma",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
        }
    )
