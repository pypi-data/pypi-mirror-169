from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from resqml22dev3.abstract_local3d_crs import AbstractLocal3DCrs
from resqml22dev3.data_object_reference import DataObjectReference
from resqml22dev3.time_uom import TimeUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class LocalTime3DCrs(AbstractLocal3DCrs):
    """Defines a local time coordinate system.

    The geometrical origin and location are defined by the elements of
    the base class AbstractLocal3dCRS. This CRS defines the time unit
    that the time-based geometries that refer to it will use.

    :ivar time_uom: Defines the unit of measure of the third (time)
        coordinates, for the geometries that refer to it.
    :ivar custom_unit_dictionary: Reference to a custom units
        dictionary, if one is used.
    """
    class Meta:
        name = "LocalTime3dCrs"
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    time_uom: Optional[Union[TimeUom, str]] = field(
        default=None,
        metadata={
            "name": "TimeUom",
            "type": "Element",
            "required": True,
            "pattern": r".*:.*",
        }
    )
    custom_unit_dictionary: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "CustomUnitDictionary",
            "type": "Element",
        }
    )
