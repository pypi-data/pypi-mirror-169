from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.abstract_object import AbstractObject

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class AbstractFeature(AbstractObject):
    """Something that has physical existence at some point during the
    exploration, development, production or abandonment of a reservoir.

    For example: It can be a boundary, a rock volume, a basin area, but
    also extends to a drilled well, a drilling rig, an injected or
    produced fluid, or a 2D, 3D, or 4D seismic survey. Features are
    divided into these categories: geologic or technical.
    """
    is_well_known: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsWellKnown",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
