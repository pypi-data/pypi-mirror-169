from __future__ import annotations
from dataclasses import dataclass

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class AbstractPoint3DArray:
    """The abstract class of 3D points implemented in a single fashion for the
    schema.

    Abstraction allows a variety of instantiations for efficiency or to
    implicitly provide additional geometric information about a data-
    object. For example, parametric points can be used to implicitly
    define a wellbore trajectory using an underlying parametric line, by
    the specification of the control points along the parametric line.
    The dimensionality of the array of 3D points is based on context
    within an instance.
    """
    class Meta:
        name = "AbstractPoint3dArray"
