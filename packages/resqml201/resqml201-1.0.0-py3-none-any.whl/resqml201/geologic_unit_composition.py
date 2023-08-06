from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


class GeologicUnitComposition(Enum):
    INTRUSIVE_CLAY = "intrusive clay "
    ORGANIC = "organic"
    INTRUSIVE_MUD = "intrusive mud "
    EVAPORITE_SALT = "evaporite salt"
    EVAPORITE_NON_SALT = "evaporite non salt"
    SEDIMENTARY_SILICLASTIC = "sedimentary siliclastic"
    CARBONATE = "carbonate"
    MAGMATIC_INTRUSIVE_GRANITOID = "magmatic intrusive granitoid"
    MAGMATIC_INTRUSIVE_PYROCLASTIC = "magmatic intrusive pyroclastic"
    MAGMATIC_EXTRUSIVE_LAVA_FLOW = "magmatic extrusive lava flow"
    OTHER_CHEMICHAL_ROCK = "other chemichal rock"
    SEDIMENTARY_TURBIDITE = "sedimentary turbidite"
