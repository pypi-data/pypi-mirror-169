from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.abstract_floating_point_array import AbstractFloatingPointArray
from resqml22.abstract_integer_array import AbstractIntegerArray
from resqml22.abstract_parametric_line_array import AbstractParametricLineArray
from resqml22.abstract_point3d_array import AbstractPoint3DArray
from resqml22.parametric_line_intersections import ParametricLineIntersections

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ParametricLineArray(AbstractParametricLineArray):
    """Defines an array of parametric lines of multiple kinds.

    For more information, see the RESQML Technical Usage Guide.
    In general, a parametric line is unbounded so the interpolant in the first or last interval is used as an extrapolating function.
    Special Cases:
    (1) Natural cubic splines with only two control points reduce to linear interpolation.
    (2) If required but not defined, tangent vectors at a spline knot are calculated from the control point data using a quadratic fit to the control point and the two adjacent control points (if internal) or, if at an edge, by a vanishing second derivative. This calculation reduces locally to a natural spline.
    (3) If not expected but provided, then extraneous information is to be ignored, e.g., tangent vectors for linear splines.
    Vertical:
    (1) Control points are (X,Y,-).
    (2) Parameter values are interpreted as depth =&gt; (X,Y,Z), where the depth to Z conversion depends on the vertical CRS direction.
    Piecewise Linear:
    (1) Control points are (P,X,Y,Z).
    (2) Piecewise interpolation in (X,Y,Z) as a linear function of P.
    Natural Cubic:
    (1) Control points are (P,X,Y,Z).
    (2) First and second derivatives at each knot are inferred from a quadratic fit to the two adjacent control points, if internal, or, if external knots, by specifying a vanishing second derivative.
    Tangential Cubic and Minimum-Curvature.
    (1) Control points are (P,X,Y,Z).
    (2) Tangent vectors are (P,TX,TY,TZ). Tangent vectors are defined as the derivative of position with respect to the parameter. If the parameter is arc-length, then the tangent vectors are unit vectors, but not otherwise.
    (3) Interpolating minimum-curvature basis functions obtained by a circular arc construction. This differs from the "drilling" algorithm in which the parameter must be arc length.
    Z Linear Cubic:
    (1) (X,Y) follow a natural cubic spline and Z follows a linear spline.
    (2) On export, to go from Z to P, the RESQML "software writer" first needs to determine the interval and then uses linearity in Z to determine P.
    (3) On import, a RESQML "software reader" converts from P to Z using piecewise linear interpolation, and from P to X and Y using natural cubic spline interpolation. Other than the differing treatment of Z from X and Y, these are completely generic interpolation algorithms.
    (4) The use of P instead of Z for interpolation allows support for over-turned reservoir structures and removes any apparent discontinuities in parametric derivatives at the spline knots.

    :ivar control_point_parameters: An array of explicit control point
        parameters for all of the control points on each of the
        parametric lines. If you cannot provide enough control point
        parameters for a parametric line, then pad with NaN values.
        BUSINESS RULE: The parametric values must be strictly
        monotonically increasing on each parametric line.
    :ivar control_points: An array of 3D points for all of the control
        points on each of the parametric lines. The number of control
        points per line is given by the KnotCount. Control points are
        ordered by lines going fastest, then by knots going slowest. If
        you cannot provide enough control points for a parametric line,
        then pad with NaN values.
    :ivar knot_count: The first dimension of the control point, control
        point parameter, and tangent vector arrays for the parametric
        splines. The Knot Count is typically chosen to be the maximum
        number of control points, parameters or tangent vectors on any
        parametric line in the array of parametric lines.
    :ivar line_kind_indices: An array of integers indicating the
        parametric line kind. 0 = vertical 1 = linear spline 2 = natural
        cubic spline 3 = tangential cubic spline 4 = Z linear cubic
        spline 5 = minimum-curvature spline null value: no line Size =
        #Lines, e.g., (1D or 2D)
    :ivar tangent_vectors: An optional array of tangent vectors for all
        of the control points on each of the tangential cubic and
        minimum-curvature parametric lines. Used only if tangent vectors
        are present. The number of tangent vectors per line is given by
        the KnotCount for these spline types. Described as a 1D array,
        the tangent vector array is divided into segments of length Knot
        Count, with null (NaN) values added to each segment to fill it
        up. Size = Knot Count x #Lines, e.g., 2D or 3D BUSINESS RULE:
        For all lines other than the cubic and minimum-curvature
        parametric lines, this array should not appear. For these line
        kinds, there should be one tangent vector for each control
        point. If a tangent vector is missing, then it is computed in
        the same fashion as for a natural cubic spline. Specifically, to
        obtain the tangent at internal knots, the control points are fit
        by a quadratic function with the two adjacent control points. At
        edge knots, the second derivative vanishes.
    :ivar parametric_line_intersections:
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
    line_kind_indices: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "LineKindIndices",
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
    parametric_line_intersections: Optional[ParametricLineIntersections] = field(
        default=None,
        metadata={
            "name": "ParametricLineIntersections",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
