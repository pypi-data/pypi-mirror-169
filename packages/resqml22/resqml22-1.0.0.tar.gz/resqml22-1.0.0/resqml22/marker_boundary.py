from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.data_object_reference import DataObjectReference
from resqml22.fluid_contact import FluidContact
from resqml22.fluid_marker import FluidMarker
from resqml22.geologic_boundary_kind import GeologicBoundaryKind

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class MarkerBoundary:
    """
    Represent interval limits associated with Witsml:WellMarkers.

    :ivar fluid_contact:
    :ivar fluid_marker:
    :ivar geologic_boundary_kind:
    :ivar qualifier:
    :ivar marker_set: This is a DataObjectReference to a WITSML
        WellboreMarkerSet
    :ivar marker: This is a DataObjectReference to a WITSML
        WellboreMarker
    :ivar interpretation:
    """
    fluid_contact: Optional[FluidContact] = field(
        default=None,
        metadata={
            "name": "FluidContact",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    fluid_marker: Optional[FluidMarker] = field(
        default=None,
        metadata={
            "name": "FluidMarker",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    geologic_boundary_kind: Optional[GeologicBoundaryKind] = field(
        default=None,
        metadata={
            "name": "GeologicBoundaryKind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    marker_set: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "MarkerSet",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    marker: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Marker",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    interpretation: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Interpretation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
