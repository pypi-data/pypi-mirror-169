from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from resqml22.boundary_feature_interpretation import BoundaryFeatureInterpretation
from resqml22.fault_throw import FaultThrow
from resqml22.length_measure import LengthMeasure
from resqml22.north_reference_kind import NorthReferenceKind
from resqml22.plane_angle_measure import PlaneAngleMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class FaultInterpretation(BoundaryFeatureInterpretation):
    """A general term for designating a boundary feature intepretation that
    corresponds to a discontinuity having a tectonic origin, identified at
    mapping or outcrop scale.

    Fault may designate true faults but also thrust surfaces. A thrust surface  is specified as a FaultInterpretation whose FaultThrow kind is "thrust" and which has the attributes: is Listric = 0, MaximumThrow = 0.

    :ivar dip_direction_north_reference_kind: If not set (absent), the
        NorthReferenceKind is Grid North.
    :ivar is_listric: Indicates if the normal fault is listric or not.
        BUSINESS RULE: Must be present if the fault is normal. Must not
        be present if the fault is not normal.
    :ivar is_sealed:
    :ivar maximum_throw:
    :ivar mean_azimuth: For this element, "mean" means "representative";
        it is not a mathematically derived mean.
    :ivar mean_dip: For this element, "mean" means "representative"; it
        is not a mathematically derived mean. It is relative to
        horizontal however horizontal is defined by the CRS.
    :ivar throw_interpretation:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    dip_direction_north_reference_kind: Optional[NorthReferenceKind] = field(
        default=None,
        metadata={
            "name": "DipDirectionNorthReferenceKind",
            "type": "Element",
        }
    )
    is_listric: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsListric",
            "type": "Element",
        }
    )
    is_sealed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSealed",
            "type": "Element",
        }
    )
    maximum_throw: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "MaximumThrow",
            "type": "Element",
        }
    )
    mean_azimuth: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "MeanAzimuth",
            "type": "Element",
        }
    )
    mean_dip: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "MeanDip",
            "type": "Element",
        }
    )
    throw_interpretation: List[FaultThrow] = field(
        default_factory=list,
        metadata={
            "name": "ThrowInterpretation",
            "type": "Element",
        }
    )
