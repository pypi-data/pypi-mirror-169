from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.abstract_point3d_array import AbstractPoint3DArray

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class PatchOfPoints:
    """A patch of points.

    In RESQML, a patch is a set or range of one kind of topological
    elements used to define part of a data-object, such as grids or
    structural data-objects.

    :ivar representation_patch_index: Optional patch index used to
        attach properties to a specific patch of the indexable elements.
    :ivar points: Geometric points (or vectors) to be attached to the
        specified indexable elements.
    """
    representation_patch_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "RepresentationPatchIndex",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    points: Optional[AbstractPoint3DArray] = field(
        default=None,
        metadata={
            "name": "Points",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
