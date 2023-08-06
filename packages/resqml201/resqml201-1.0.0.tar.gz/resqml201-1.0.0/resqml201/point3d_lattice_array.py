from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from resqml201.abstract_point3d_array import AbstractPoint3DArray
from resqml201.point3d import Point3D
from resqml201.point3d_offset import Point3DOffset

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class Point3DLatticeArray(AbstractPoint3DArray):
    """Describes a lattice array of points obtained by sampling from along a
    multi-dimensional lattice.

    Each dimension of the lattice can be uniformly or irregularly
    spaced.

    :ivar all_dimensions_are_orthogonal: The optional element that
        indicates that the offset vectors for each direction are
        mutually orthogonal to each other. This meta-information is
        useful to remove any doubt of orthogonality in case of numerical
        precision issues. BUSINESS RULE: If you don't know it or if only
        one lattice dimension is given, do not provide this element.
    :ivar origin: The origin location of the lattice given as XYZ
        coordinates.
    :ivar offset:
    """
    class Meta:
        name = "Point3dLatticeArray"

    all_dimensions_are_orthogonal: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AllDimensionsAreOrthogonal",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    origin: Optional[Point3D] = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    offset: List[Point3DOffset] = field(
        default_factory=list,
        metadata={
            "name": "Offset",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "min_occurs": 1,
        }
    )
