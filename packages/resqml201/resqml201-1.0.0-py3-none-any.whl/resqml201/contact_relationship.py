from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


class ContactRelationship(Enum):
    """
    The enumerations that specify the role of the contacts in a contact
    interpretation as described in the attributes below.

    :cvar FRONTIER_FEATURE_TO_FRONTIER_FEATURE: A contact between two
        frontier features to close a volume of interest.
    :cvar GENETIC_BOUNDARY_TO_FRONTIER_FEATURE: A linear contact between
        a genetic boundary interpretation and a frontier feature
        (horizon/frontier contact).
    :cvar GENETIC_BOUNDARY_TO_GENETIC_BOUNDARY: A linear contact between
        two genetic boundary interpretations (horizon/horizon contact).
    :cvar GENETIC_BOUNDARY_TO_TECTONIC_BOUNDARY: A linear contact
        between a genetic boundary interpretation and a tectonic
        boundary interpretation (horizon/fault contact).
    :cvar STRATIGRAPHIC_UNIT_TO_FRONTIER_FEATURE: A surface contact
        between a stratigraphic unit interpretation and a frontier
        feature (contact closing a volume on a frontier feature that is
        a technical feature).
    :cvar STRATIGRAPHIC_UNIT_TO_STRATIGRAPHIC_UNIT: A surface contact
        between two stratigraphic unit interpretations (unit/unit
        contact).
    :cvar TECTONIC_BOUNDARY_TO_FRONTIER_FEATURE: A linear contact
        between a tectonic boundary interpretation and a frontier
        feature (fault/frontier contact).
    :cvar TECTONIC_BOUNDARY_TO_GENETIC_BOUNDARY: A linear contact
        between a tectonic boundary interpretation and a genetic
        boundary interpretation (fault/horizon contact).
    :cvar TECTONIC_BOUNDARY_TO_TECTONIC_BOUNDARY: A linear contact
        between two tectonic boundary interpretations (fault/fault
        contact).
    """
    FRONTIER_FEATURE_TO_FRONTIER_FEATURE = "frontier feature to frontier feature"
    GENETIC_BOUNDARY_TO_FRONTIER_FEATURE = "genetic boundary to frontier feature"
    GENETIC_BOUNDARY_TO_GENETIC_BOUNDARY = "genetic boundary to genetic boundary"
    GENETIC_BOUNDARY_TO_TECTONIC_BOUNDARY = "genetic boundary to tectonic boundary"
    STRATIGRAPHIC_UNIT_TO_FRONTIER_FEATURE = "stratigraphic unit to frontier feature"
    STRATIGRAPHIC_UNIT_TO_STRATIGRAPHIC_UNIT = "stratigraphic unit to stratigraphic unit"
    TECTONIC_BOUNDARY_TO_FRONTIER_FEATURE = "tectonic boundary to frontier feature"
    TECTONIC_BOUNDARY_TO_GENETIC_BOUNDARY = "tectonic boundary to genetic boundary"
    TECTONIC_BOUNDARY_TO_TECTONIC_BOUNDARY = "tectonic boundary to tectonic boundary"
