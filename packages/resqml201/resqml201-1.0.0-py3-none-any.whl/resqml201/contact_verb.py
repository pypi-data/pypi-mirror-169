from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


class ContactVerb(Enum):
    """
    Enumerations for the verbs that can be used to define the impact on the
    construction of the model of the geological event that created the binary
    contact.

    :cvar SPLITS: Specifies that the fault has opened a pair of fault
        lips in a horizon.
    :cvar INTERRUPTS: Operation on which an "unconformable" genetic
        boundary interpretation interrupts another genetic boundary
        interpretation or a stratigraphic unit interpretation.
    :cvar CONTAINS: Precise use of this attribute to be determined
        during testing.
    :cvar CONFORMS: Defines surface contact between two stratigraphic
        units.
    :cvar ERODES: Defines surface contact between two stratigraphic
        units.
    :cvar STOPS_AT: Defines if a tectonic boundary interpretation stops
        at another tectonic boundary interpretation. Also used for
        genetic unit to frontier feature, fault to frontier feature, and
        sedimentary unit to frontier feature.
    :cvar CROSSES: Defines if a tectonic boundary interpretation crosses
        another tectonic boundary interpretation.
    :cvar INCLUDES: Precise use of this attribute will be determined
        during testing.
    """
    SPLITS = "splits"
    INTERRUPTS = "interrupts"
    CONTAINS = "contains"
    CONFORMS = "conforms"
    ERODES = "erodes"
    STOPS_AT = "stops at"
    CROSSES = "crosses"
    INCLUDES = "includes"
