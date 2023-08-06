from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


class MdReference(Enum):
    """Reference location for the measured depth datum (MdDatum).

    The type of local or permanent reference datum for vertical gravity
    based (i.e., elevation and vertical depth) and measured depth
    coordinates within the context of a well. This list includes local
    points (e.g., kelly bushing) used as a datum and vertical reference
    datums (e.g., mean sea level).

    :cvar GROUND_LEVEL:
    :cvar KELLY_BUSHING:
    :cvar MEAN_SEA_LEVEL: A tidal datum. The arithmetic mean of hourly
        heights observed over the National Tidal Datum Epoch (19 years).
    :cvar DERRICK_FLOOR:
    :cvar CASING_FLANGE: A flange affixed to the top of the casing
        string used to attach production equipment.
    :cvar ARBITRARY_POINT: This value should not be used for drilled
        wells. All reasonable attempts should be made to determine the
        appropriate value.
    :cvar CROWN_VALVE:
    :cvar ROTARY_BUSHING:
    :cvar ROTARY_TABLE:
    :cvar SEA_FLOOR:
    :cvar LOWEST_ASTRONOMICAL_TIDE: The lowest tide level over the
        duration of the National Tidal Datum Epoch (19 years).
    :cvar MEAN_HIGHER_HIGH_WATER: A tidal datum. The average of the
        higher high water height of each tidal day observed over the
        National Tidal Datum Epoch (19 years).
    :cvar MEAN_HIGH_WATER: A tidal datum. The average of all the high
        water heights observed over the National Tidal Datum Epoch (19
        years).
    :cvar MEAN_LOWER_LOW_WATER: A tidal datum. The average of the lower
        low water height of each tidal day observed over the National
        Tidal Datum Epoch (19 years ).
    :cvar MEAN_LOW_WATER: A tidal datum. The average of all the low
        water heights observed over the National Tidal Datum Epoch (19
        years).
    :cvar MEAN_TIDE_LEVEL: A tidal datum. The arithmetic mean of mean
        high water and mean low water. Same as half-tide level.
    :cvar KICKOFF_POINT: This value is not expected to be used in most
        typical situations. All reasonable attempts should be made to
        determine the appropriate value.
    """
    GROUND_LEVEL = "ground level"
    KELLY_BUSHING = "kelly bushing"
    MEAN_SEA_LEVEL = "mean sea level"
    DERRICK_FLOOR = "derrick floor"
    CASING_FLANGE = "casing flange"
    ARBITRARY_POINT = "arbitrary point"
    CROWN_VALVE = "crown valve"
    ROTARY_BUSHING = "rotary bushing"
    ROTARY_TABLE = "rotary table"
    SEA_FLOOR = "sea floor"
    LOWEST_ASTRONOMICAL_TIDE = "lowest astronomical tide"
    MEAN_HIGHER_HIGH_WATER = "mean higher high water"
    MEAN_HIGH_WATER = "mean high water"
    MEAN_LOWER_LOW_WATER = "mean lower low water"
    MEAN_LOW_WATER = "mean low water"
    MEAN_TIDE_LEVEL = "mean tide level"
    KICKOFF_POINT = "kickoff point"
