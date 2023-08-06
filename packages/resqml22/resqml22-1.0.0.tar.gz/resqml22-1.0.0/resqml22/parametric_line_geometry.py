from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.abstract_floating_point_array import AbstractFloatingPointArray
from resqml22.abstract_parametric_line_geometry import AbstractParametricLineGeometry
from resqml22.abstract_point3d_array import AbstractPoint3DArray

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ParametricLineGeometry(AbstractParametricLineGeometry):
    """Defines a parametric line of any kind.

    For more information on the supported parametric lines, see
    ParametricLineArray.

    :ivar control_point_parameters: An array of explicit control point
        parameters for the control points on the parametric line.
        BUSINESS RULE: The size MUST match the number of control points.
        BUSINESS RULE: The parametric values MUST be strictly
        monotonically increasing on the parametric line.
    :ivar control_points: An array of 3D points for the control points
        on the parametric line.
    :ivar knot_count: Number of spline knots in the parametric line.
    :ivar line_kind_index: Integer indicating the parametric line kind 0
        for vertical 1 for linear spline 2 for natural cubic spline 3
        for cubic spline 4 for z linear cubic spline 5 for minimum-
        curvature spline (-1) for null: no line
    :ivar tangent_vectors: An optional array of tangent vectors for each
        control point on the cubic and minimum-curvature parametric
        lines. Used only if tangent vectors are present. If a tangent
        vector is missing, then it is computed in the same fashion as
        for a natural cubic spline. Specifically, to obtain the tangent
        at internal knots, the control points are fit by a quadratic
        function with the two adjacent control points. At edge knots,
        the second derivative vanishes.
    """
    control_point_parameters: Optional[AbstractFloatingPointArray] = field(
        default=None,
        metadata={
            "name": "ControlPointParameters",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    control_points: Optional[AbstractPoint3DArray] = field(
        default=None,
        metadata={
            "name": "ControlPoints",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    knot_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "KnotCount",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
            "min_inclusive": 1,
        }
    )
    line_kind_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "LineKindIndex",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    tangent_vectors: Optional[AbstractPoint3DArray] = field(
        default=None,
        metadata={
            "name": "TangentVectors",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
