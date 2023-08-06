from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.data_object_reference import DataObjectReference
from resqml201.obj_geologic_unit_feature import ObjGeologicUnitFeature

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ObjStratigraphicUnitFeature(ObjGeologicUnitFeature):
    """A stratigraphic unit that can have a well-known (e.g., "Jurassic")
    chronostratigraphic top and chronostratigraphic bottom.

    These chronostratigraphic units have no associated interpretations
    or representations. BUSINESS RULE: The name must reference a well-
    known chronostratigraphic unit (such as "Jurassic"), for example,
    from the International Commission on Stratigraphy
    (http://www.stratigraphy.org).
    """
    class Meta:
        name = "obj_StratigraphicUnitFeature"

    chronostratigraphic_bottom: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "ChronostratigraphicBottom",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    chronostratigraphic_top: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "ChronostratigraphicTop",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
