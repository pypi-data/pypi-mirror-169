from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


class OrganizationKind(Enum):
    """Enumerations used to indicate a specific type of organization.

    See attributes below.

    :cvar EARTH_MODEL: An organization composed of the other types of
        organizations listed here.
    :cvar FLUID: A volume organization composed of fluid boundaries and
        phase units.
    :cvar STRATIGRAPHIC: A volume organization composed of geologic
        features, such as geobodies, stratigraphic units, and
        boundaries.
    :cvar STRUCTURAL: A surface organization composed of geologic
        features, such as faults, horizons, and frontier boundaries.
    """
    EARTH_MODEL = "earth model"
    FLUID = "fluid"
    STRATIGRAPHIC = "stratigraphic"
    STRUCTURAL = "structural"
