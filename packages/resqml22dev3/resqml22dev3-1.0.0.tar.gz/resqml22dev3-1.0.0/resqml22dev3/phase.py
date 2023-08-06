from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


class Phase(Enum):
    """The enumeration of the possible rock fluid unit phases in a hydrostatic
    column.

    The seal is considered here as a part (the coverage phase) of a
    hydrostatic column.

    :cvar AQUIFER: Volume of the hydrostatic column for which only the
        aqueous phase is mobile. Typically below the Pc (hydrocarbon-
        water) = 0 free fluid surface.
    :cvar GAS_CAP: Volume of the hydrostatic column for which only the
        gaseous phase is mobile. Typically above the Pc (gas-oil) = 0
        free fluid surface.
    :cvar OIL_COLUMN: Volume of the hydrostatic column for which only
        the oleic and aqueous phases may be mobile. Typically below the
        gas-oil Pc = 0 free fluid surface. Pc (gas-oil) = 0 free fluid
        surface.
    :cvar SEAL: Impermeable volume that provides the seal for a
        hydrostatic fluid column.
    """
    AQUIFER = "aquifer"
    GAS_CAP = "gas cap"
    OIL_COLUMN = "oil column"
    SEAL = "seal"
