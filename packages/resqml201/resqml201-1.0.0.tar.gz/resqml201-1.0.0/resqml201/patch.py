from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class Patch:
    """Set or range of one kind of topological element used to define part of a
    data-object; this concept exists for grid and structural data-objects.

    Subset of a specified kind of indexable element of a representation,
    associated with a patch index. The patch index is used to define the
    relative order for the elements. It may also be used to access
    patches of indexable elements directly for geometry, properties, or
    relationships. Patches are used to remove any ambiguity in data
    ordering among the indexable elements. For example, the triangle
    indexing of a triangulated set representation consists of multiple
    triangles, each with a patch index. This index specifies the
    relative ordering of the triangle patches. Those data-objects that
    inherit a patch index from the abstract class of patches all include
    the word "Patch" as part of their name, e.g., TrianglePatch.

    :ivar patch_index: Local index of the patch, making it unique within
        the representation.
    """
    patch_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "PatchIndex",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
