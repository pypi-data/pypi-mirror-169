from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.genetic_boundary_kind import GeneticBoundaryKind
from resqml201.obj_boundary_feature import ObjBoundaryFeature
from resqml201.timestamp import Timestamp

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ObjGeneticBoundaryFeature(ObjBoundaryFeature):
    """A boundary between two units produced by a contrast between two deposits
    that occurred at two different geologic time periods.

    For types, see GeneticBoundaryKind.
    """
    class Meta:
        name = "obj_GeneticBoundaryFeature"

    genetic_boundary_kind: Optional[GeneticBoundaryKind] = field(
        default=None,
        metadata={
            "name": "GeneticBoundaryKind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    absolute_age: Optional[Timestamp] = field(
        default=None,
        metadata={
            "name": "AbsoluteAge",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
