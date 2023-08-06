from __future__ import annotations
from dataclasses import dataclass

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class AbstractTimeInterval:
    """The abstract superclass for all RESQML time intervals.

    The super class that contains all types of intervals considered in
    geolog, including  those based on chronostratigraphy, the duration
    of geological events, and time intervals used in reservoir
    simulation (e.g., time step).
    """
