from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class OrientedMacroFace:
    """An element of a volume shell that is defined by a set of oriented faces
    belonging to boundable patches. A macroface may describe a contact between:

    - two structural, stratigraphic, or fluid units
    - one boundary feature (fault or frontier) and a unit.
    A face is a bounded open subset of a plane or a curved surface in 3D, delimited by an outer contour and zero, one, or more inner contours describing holes.

    :ivar patch_index_of_representation: Create the triangulation and 2D
        grid representation for which the patches match the macro faces.
    :ivar representation_index: Identifies the representation by its
        index, in the list of representations contained in the
        organization.
    :ivar side_is_plus:
    """
    patch_index_of_representation: Optional[int] = field(
        default=None,
        metadata={
            "name": "PatchIndexOfRepresentation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    representation_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "RepresentationIndex",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    side_is_plus: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SideIsPlus",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
