from __future__ import annotations
from dataclasses import dataclass
from resqml201.abstract_feature import AbstractFeature

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class AbstractGeologicFeature(AbstractFeature):
    """Objects that exist a priori, in the natural world, for example: the rock
    formations and how they are positioned with regard to each other; the
    fluids that are present before production; or the position of the
    geological intervals with respect to each.

    Some of these objects are static—such as geologic intervals---while
    others are dynamic—such as fluids; their properties, geometries, and
    quantities may change over time during the course of field
    production. RESQML has these types of features: geologic and
    technical.
    """
