from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


class MdDomain(Enum):
    """
    Different types of measured depths.

    :cvar DRILLER: The original depths recorded while drilling a well or
        LWD or MWD.
    :cvar LOGGER: Depths recorded when logging a well, which are in
        general considered to be more accurate than driller's depth.
    """
    DRILLER = "driller"
    LOGGER = "logger"
