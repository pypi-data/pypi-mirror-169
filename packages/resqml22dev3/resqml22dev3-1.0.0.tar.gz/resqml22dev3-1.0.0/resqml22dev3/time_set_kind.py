from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


class TimeSetKind(Enum):
    """
    Indicates that the collection of properties shares this time relationship,
    if any.

    :cvar SINGLE_TIME: Indicates that the collection contains only
        property values associated with a single time index, i.e., time
        identity can be ascertained from the time index itself, without
        knowledge of the time.
    :cvar SINGLE_TIME_SERIES: Indicates that the collection contains
        only property values associated with a single time series, so
        that time identity can be ascertained from the time index
        itself, without knowledge of the time.
    :cvar EQUIVALENT_TIMES: Indicates that the collection of properties
        is at equivalent times, e.g., a 4D seismic data set and a
        reservoir simulation model at comparable times. For a more
        specific relationship, select single time.
    :cvar NOT_A_TIME_SET: Indicates that the property collection is not
        related by time.
    """
    SINGLE_TIME = "single time"
    SINGLE_TIME_SERIES = "single time series"
    EQUIVALENT_TIMES = "equivalent times"
    NOT_A_TIME_SET = "not a time set"
