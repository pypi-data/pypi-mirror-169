from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


class ContactVerb(Enum):
    """
    Enumerations for the verbs that can be used to define the impact on the
    construction of the model of the geological event that created the binary
    contact.

    :cvar STOPS:
    :cvar INTERRUPTS: Operation on which an "unconformable" genetic
        boundary interpretation interrupts another genetic boundary
        interpretation or a stratigraphic unit interpretation.
    :cvar CROSSES: Defines if a tectonic boundary interpretation crosses
        another tectonic boundary interpretation.
    """
    STOPS = "stops"
    INTERRUPTS = "interrupts"
    CROSSES = "crosses"
