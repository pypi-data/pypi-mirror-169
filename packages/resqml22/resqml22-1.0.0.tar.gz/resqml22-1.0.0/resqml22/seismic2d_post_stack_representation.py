from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.abstract_representation import AbstractRepresentation
from resqml22.data_object_reference import DataObjectReference
from resqml22.floating_point_lattice_array import FloatingPointLatticeArray
from resqml22.integer_lattice_array import IntegerLatticeArray

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class Seismic2DPostStackRepresentation(AbstractRepresentation):
    """The feature of this representation should be the same survey feature as
    the associated PolylineRepresentation represents.. The indexing convention
    (mainly for associated properties) is :

    - Trace sample goes fastest
    - Then polyline node slowest
    The indexing convention only applies to HDF datasets (not SEGY file).
    A whole SEGY file can be referenced in properties of this representation, but not partial files.

    :ivar seismic_line_sub_sampling: This array must be one dimension
        and count must be the node count in the associated seismic line
        i.e., polylineRepresentation. The index is based on array
        indexing, not on index labeling of traces. The values of the
        integer lattice array are the increments between 2 consecutive
        subsampled nodes.
    :ivar trace_sampling: Defines the sampling in the vertical dimension
        of the representation. This array must be one dimension. The
        values are given with respect to the associated local CRS.
    :ivar seismic_line_representation:
    :ivar local_crs:
    """
    class Meta:
        name = "Seismic2dPostStackRepresentation"
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    seismic_line_sub_sampling: Optional[IntegerLatticeArray] = field(
        default=None,
        metadata={
            "name": "SeismicLineSubSampling",
            "type": "Element",
            "required": True,
        }
    )
    trace_sampling: Optional[FloatingPointLatticeArray] = field(
        default=None,
        metadata={
            "name": "TraceSampling",
            "type": "Element",
            "required": True,
        }
    )
    seismic_line_representation: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "SeismicLineRepresentation",
            "type": "Element",
            "required": True,
        }
    )
    local_crs: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "LocalCrs",
            "type": "Element",
            "required": True,
        }
    )
