from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.obj_boundary_feature import ObjBoundaryFeature
from resqml201.tectonic_boundary_kind import TectonicBoundaryKind

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ObjTectonicBoundaryFeature(ObjBoundaryFeature):
    """A boundary caused by tectonic movement or metamorphism, such as a fault
    or a fracture.

    For types, see TectonicBoundaryKind.
    """
    class Meta:
        name = "obj_TectonicBoundaryFeature"

    tectonic_boundary_kind: Optional[TectonicBoundaryKind] = field(
        default=None,
        metadata={
            "name": "TectonicBoundaryKind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
