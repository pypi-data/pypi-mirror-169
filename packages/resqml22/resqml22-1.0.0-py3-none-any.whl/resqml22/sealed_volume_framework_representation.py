from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from resqml22.data_object_reference import DataObjectReference
from resqml22.representation_set_representation import RepresentationSetRepresentation
from resqml22.volume_region import VolumeRegion

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class SealedVolumeFrameworkRepresentation(RepresentationSetRepresentation):
    """A strict boundary representation (BREP), which represents the volume
    region by assembling together shells.

    BUSINESS RULE: The sealed structural framework must be part of the
    same earth model as this sealed volume framework.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    based_on: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "BasedOn",
            "type": "Element",
            "required": True,
        }
    )
    regions: List[VolumeRegion] = field(
        default_factory=list,
        metadata={
            "name": "Regions",
            "type": "Element",
            "min_occurs": 1,
        }
    )
