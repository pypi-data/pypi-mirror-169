from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class ExistenceKind(Enum):
    """A list of lifecycle states like actual, required, planned, predicted,
    etc.

    These are used to qualify any top-level element (from Epicentre
    2.1).

    :cvar ACTUAL: The object actually exists (from Epicentre 2.1).
    :cvar PLANNED: The object exists only in the planning stage (from
        Epicentre 2.1).
    :cvar SIMULATED: Created, artificially, as an artifact of
        processing, to replace or to stand for one or more similar
        objects. Often referred to as model (from Epicentre 2.1).
    """
    ACTUAL = "actual"
    PLANNED = "planned"
    SIMULATED = "simulated"
