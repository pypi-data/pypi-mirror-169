from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.abstract_floating_point_array import AbstractFloatingPointArray
from resqml22.abstract_point3d_array import AbstractPoint3DArray

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class Point3DZvalueArray(AbstractPoint3DArray):
    """An array of points defined by applying a Z value on top of an existing
    array of points, XYZ, where Z is ignored. Used in these cases:

    - in 2D for defining geometry of one patch of a 2D grid representation.
    - for extracting nodal geometry from one grid representation for use in another.

    :ivar supporting_geometry: Geometry defining the X and Y
        coordinates.
    :ivar zvalues: The values for Z coordinates
    """
    class Meta:
        name = "Point3dZValueArray"

    supporting_geometry: Optional[AbstractPoint3DArray] = field(
        default=None,
        metadata={
            "name": "SupportingGeometry",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    zvalues: Optional[AbstractFloatingPointArray] = field(
        default=None,
        metadata={
            "name": "ZValues",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
