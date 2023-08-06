from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.geobody3d_shape import Geobody3DShape
from resqml201.obj_geologic_unit_interpretation import ObjGeologicUnitInterpretation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ObjGeobodyInterpretation(ObjGeologicUnitInterpretation):
    """
    A type of rock feature, this class identifies if a rock feature is a
    geobody with any qualifications on the interpretation of the geobody.
    """
    class Meta:
        name = "obj_GeobodyInterpretation"

    geobody3d_shape: Optional[Geobody3DShape] = field(
        default=None,
        metadata={
            "name": "Geobody3dShape",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
