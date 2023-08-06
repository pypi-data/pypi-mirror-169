from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.abstract_floating_point_array import AbstractFloatingPointArray
from resqml22.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class TvdInformation:
    """
    Business rule:

    :ivar node_tvd_values: Count must be equal to count of nodes of the
        associated wellbore frame. The direction of the supporting axis
        is given by the LocalDepth3dCrs itself. It is necessary to get
        the information to know what are positive or negative values.
        The values are given with respect to the TvdDatum, not with
        respect to the ZOffest of the LocalDepth3dCrs The UOM is the one
        specified in the LocalDepth3dCrs.
    :ivar tvd_datum: The direction of the supporting axis is given by
        the LocalDepth3dCrs itself. It is necessary to get the
        information to know what is a positive or a negative value. The
        value is given with respect to the ZOffset of the
        LocalDepth3dCrs. The UOM is the one specified in the
        LocalDepth3dCrs.
    :ivar tvd_reference:
    :ivar local_depth3d_crs:
    """
    node_tvd_values: Optional[AbstractFloatingPointArray] = field(
        default=None,
        metadata={
            "name": "NodeTvdValues",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    tvd_datum: Optional[float] = field(
        default=None,
        metadata={
            "name": "TvdDatum",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    tvd_reference: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "TvdReference",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    local_depth3d_crs: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "LocalDepth3dCrs",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
