from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.abstract_double_array import AbstractDoubleArray
from resqml201.abstract_integer_array import AbstractIntegerArray
from resqml201.abstract_parametric_line_array import AbstractParametricLineArray
from resqml201.abstract_point3d_array import AbstractPoint3DArray
from resqml201.parametric_line_intersections import ParametricLineIntersections

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ParametricLineArray(AbstractParametricLineArray):
    """Defines an array of parametric lines of multiple kinds.

    These are the documented parametric line kinds; see additional information below:
    0 = vertical
    1 = linear spline (piecewise linear)
    2 = natural cubic spline
    3 = cubic spline
    4 = Z linear cubic spline
    5 = minimum-curvature spline
    (-1) = null: no line
    If isBounded=true in the line definition, then any out of range parametric values in the parametric points are truncated to the first or last control point. Otherwise, the interpolant in the first or last interval is used as an extrapolating function.
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
    (3) Interpolating basis functions are obtained by specifying values and second derivatives at the knots.
    Cubic and Minimum-Curvature.
    (1) Control points are (P,X,Y,Z).
    (2) Tangent vectors are (P,TX,TY,TZ). Tangent vectors are defined as the derivative of position with respect to the parameter. If the parameter is arc-length, then the tangent vectors are unit vectors, but not otherwise.
    (3) Interpolating cubic basis functions obtained by specifying values and first derivatives at the knots.
    (4) Interpolating minimum-curvature basis functions obtained by a circular arc construction that is constrained by the knot data. This differs from the unconstrained "drilling" algorithm in which the knot locations are not independent but for which the parameter must be arc length.
    Z Linear Cubic:
    (1) (X,Y) follow a natural cubic spline and Z follows a linear spline.
    (2) Parametric values cannot be freely chosen but are instead defined to take the values of 0,,,.N for a line with N intervals, N+1 control points.
    (3) On export, to go from Z to P, the RESQML "software writer" first needs to determine the interval and then uses linearity in Z to determine P. For the control points, the P values are 0...N and for values of Z, other than the control points, intermediate values of P arise.
    (4) On import, a RESQML "software reader" converts from P to Z using piecewise linear interpolation, and from P to X and Y using natural cubic spline interpolation. Other than the differing treatment of Z from X and Y, these are completely generic interpolation algorithms.
    (5) The use of P instead of Z for interpolation allows support for over-turned reservoir structures and removes any apparent discontinuities in parametric derivatives at the spline knots.

    :ivar control_point_parameters: An optional array of explicit
        control point parameters for all of the control points on each
        of the parametric lines. Used only if control point parameters
        are present. The number of explicit control point parameters per
        line is given by the count of non-null parameters on each line.
        Described as a 1D array, the control point parameter array is
        divided into segments of length count, with null (NaN) values
        added to each segment to fill it up. Size = count x #Lines,
        e.g., 2D or 3D BUSINESS RULE: This count should be zero for
        vertical and Z linear cubic parametric lines. For all other
        parametric line kinds, there should be one control point
        parameter for each control point. NOTES: (1) Vertical parametric
        lines do not require control point parameters (2) Z linear cubic
        splines have implicitly defined parameters. For a line with N
        intervals (N+1 control points), the parametric values are
        P=0,...,N. BUSINESS RULE: The parametric values must be strictly
        monotonically increasing on each parametric line.
    :ivar control_points: An array of 3D points for all of the control
        points on each of the parametric lines. The number of control
        points per line is given by the count of non-null 3D points on
        each line. Described as a 1D array, the control point array is
        divided into segments of length count, with null (NaN) values
        added to each segment to fill it up. Size = count x #Lines,
        e.g., 2D or 3D
    :ivar knot_count: The first dimension of the control point, control
        point parameter, and tangent vector arrays for the parametric
        splines. The Knot Count is typically chosen to be the maximum
        number of control points, parameters or tangent vectors on any
        parametric line in the array of parametric lines.
    :ivar line_kind_indices: An array of integers indicating the
        parametric line kind. 0 = vertical 1 = linear spline 2 = natural
        cubic spline 3 = cubic spline 4 = Z linear cubic spline 5 =
        minimum-curvature spline (-1) = null: no line Size = #Lines,
        e.g., (1D or 2D)
    :ivar tangent_vectors: An optional array that is of tangent vectors
        for all of the control points on each of the cubic and minimum-
        curvature parametric lines. Used only if tangent vectors are
        present. The number of tangent vectors per line is given by the
        count of non-null tangent vectors on each of these line kinds.
        Described as a 1D array, the tangent vector array is divided
        into segments of length count, with null (NaN) values added to
        each segment to fill it up. Size = count x #Lines, e.g., 2D or
        3D BUSINESS RULE: For all lines other than the cubic and
        minimum-curvature parametric lines, this count is zero. For
        these line kinds, there is one tangent vector for each control
        point. If a tangent vector is missing, then it is computed in
        the same fashion as for a natural cubic spline. Specifically, to
        obtain the tangent at internal knots, the control points are fit
        by a quadratic function with the two adjacent control points. At
        edge knots, the second derivative vanishes.
    :ivar parametric_line_intersections:
    """
    control_point_parameters: Optional[AbstractDoubleArray] = field(
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
