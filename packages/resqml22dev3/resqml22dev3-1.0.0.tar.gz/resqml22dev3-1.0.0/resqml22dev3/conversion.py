from __future__ import annotations
from dataclasses import dataclass
from resqml22dev3.general_conversion_property_type import GeneralConversionPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class Conversion(GeneralConversionPropertyType):
    """
    gml:conversion is an association role to the coordinate conversion used to
    define the derived CRS.
    """
    class Meta:
        name = "conversion"
        namespace = "http://www.opengis.net/gml/3.2"
