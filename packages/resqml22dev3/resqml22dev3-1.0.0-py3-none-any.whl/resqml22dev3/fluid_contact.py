from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


class FluidContact(Enum):
    """
    Enumerated values used to indicate a specific type of fluid boundary
    interpretation.

    :cvar FREE_WATER_CONTACT: A surface defined by vanishing capillary
        pressure between the water and hydrocarbon phases.
    :cvar GAS_OIL_CONTACT: A surface defined by vanishing capillary
        pressure between the gas and oil hydrocarbon phases.
    :cvar GAS_WATER_CONTACT: A surface defined by vanishing capillary
        pressure between the water and gas hydrocarbon phases.
    :cvar SEAL: Identifies a break in the hydrostatic column.
    :cvar WATER_OIL_CONTACT: A surface defined by vanishing capillary
        pressure between the water and oil hydrocarbon phases.
    """
    FREE_WATER_CONTACT = "free water contact"
    GAS_OIL_CONTACT = "gas oil contact"
    GAS_WATER_CONTACT = "gas water contact"
    SEAL = "seal"
    WATER_OIL_CONTACT = "water oil contact"
