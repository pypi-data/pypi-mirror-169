from __future__ import annotations
from dataclasses import dataclass
from resqml201.obj_genetic_boundary_feature import ObjGeneticBoundaryFeature

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class GeneticBoundaryFeature(ObjGeneticBoundaryFeature):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
