from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.deposition_mode import DepositionMode
from resqml201.length_measure import LengthMeasure
from resqml201.obj_geologic_unit_interpretation import ObjGeologicUnitInterpretation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ObjStratigraphicUnitInterpretation(ObjGeologicUnitInterpretation):
    """
    Interpretation of a stratigraphic unit which includes the knowledge of the
    top, the bottom, the deposition mode.

    :ivar deposition_mode: BUSINESS RULE / The Deposition mode for a
        Geological Unit MUST be conssitent with the Boundary Relations
        of A Genetic Boundary. If it is not the case the Boundary
        Relation declaration is retained.
    :ivar max_thickness:
    :ivar min_thickness:
    """
    class Meta:
        name = "obj_StratigraphicUnitInterpretation"

    deposition_mode: Optional[DepositionMode] = field(
        default=None,
        metadata={
            "name": "DepositionMode",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    max_thickness: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "MaxThickness",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    min_thickness: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "MinThickness",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
