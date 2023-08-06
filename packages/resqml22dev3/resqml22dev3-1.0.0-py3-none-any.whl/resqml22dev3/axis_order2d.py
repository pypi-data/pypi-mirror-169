from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class AxisOrder2D(Enum):
    """
    Defines the coordinate system axis order of the global CRS using the axis
    names (from EPSG database).

    :cvar EASTING_NORTHING: The first axis is easting and the second
        axis is northing.
    :cvar NORTHING_EASTING: The first axis is northing and the second
        asis is easting.
    :cvar WESTING_SOUTHING: The first axis is westing and the second
        axis is southing.
    :cvar SOUTHING_WESTING: The first axis is southing and the second
        axis is westing.
    :cvar NORTHING_WESTING: the first axis is northing and the second
        axis is westing.
    :cvar WESTING_NORTHING: the first axis is westing and the second
        axis is northing.
    """
    EASTING_NORTHING = "easting northing"
    NORTHING_EASTING = "northing easting"
    WESTING_SOUTHING = "westing southing"
    SOUTHING_WESTING = "southing westing"
    NORTHING_WESTING = "northing westing"
    WESTING_NORTHING = "westing northing"
