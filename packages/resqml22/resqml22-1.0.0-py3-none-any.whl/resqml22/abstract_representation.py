from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.abstract_object import AbstractObject
from resqml22.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class AbstractRepresentation(AbstractObject):
    """The parent class of all specialized digital descriptions, which may
    provide a representation of any kind of representable object such as
    interpretations, technical features, or WITSML wellbores. It may be either
    of these:

    - based on a topology and contains the geometry of this digital description.
    - based on the topology or the geometry of another representation.
    Not all representations require a defined geometry. For example, a defined geometry is not required for block-centered grids or wellbore frames. For representations without geometry, a software writer may provide null (NaN) values in the local 3D CRS, which is mandatory.
    TimeIndex is provided to describe time-dependent geometry.

    :ivar realization_index: Optional element indicating a realization
        id (metadata). Used if the representation is created by a
        stochastic or Monte Carlo method. Representations with the same
        id are based on the same set of random values.
    :ivar represented_object: BUSINESS RULE: The data object represented
        by the representation is either an interpretation or a technical
        feature.
    """
    realization_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "RealizationIndex",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "min_inclusive": 1,
        }
    )
    represented_object: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "RepresentedObject",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
