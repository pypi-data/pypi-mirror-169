from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.abstract_integer_array import AbstractIntegerArray

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class UnstructuredGridHingeNodeFaces:
    """Hinge nodes define a triangulated interpolation on a cell face.

    In practice, they arise on the K faces of column layer cells and are
    used to add additional geometric resolution to the shape of the
    cell. The specification of triangulated interpolation also uniquely
    defines the interpolation schema on the cell face, and hence the
    cell volume. For an unstructured cell grid, the hinge node faces
    need to be defined explicitly. This hinge node faces object is
    optional and is only expected to be used if the hinge node faces
    higher order grid point attachment arises. Hinge node faces are not
    supported for property attachment. Instead use a subrepresentation
    or an attachment kind of faces or faces per cell. BUSINESS RULE:
    Each cell must have either 0 or 2 hinge node faces, so that the two
    hinge nodes for the cell may be used to define a cell center line
    and a cell thickness.

    :ivar count: Number of K faces. This count must be positive.
    :ivar face_indices: List of faces to be identified as K faces for
        hinge node geometry attachment. BUSINESS RULE: Array length
        equals K face count.
    """
    count: Optional[int] = field(
        default=None,
        metadata={
            "name": "Count",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    face_indices: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "FaceIndices",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
