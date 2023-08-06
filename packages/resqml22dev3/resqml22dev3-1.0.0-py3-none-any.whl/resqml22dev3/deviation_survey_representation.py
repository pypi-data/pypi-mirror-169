from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from resqml22dev3.abstract_floating_point_array import AbstractFloatingPointArray
from resqml22dev3.abstract_representation import AbstractRepresentation
from resqml22dev3.data_object_reference import DataObjectReference
from resqml22dev3.length_uom import LengthUom
from resqml22dev3.plane_angle_uom import PlaneAngleUom
from resqml22dev3.single_point_geometry import SinglePointGeometry

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class DeviationSurveyRepresentation(AbstractRepresentation):
    """Specifies the station data from a deviation survey.

    The deviation survey does not provide a complete specification of
    the geometry of a wellbore trajectory. Although a minimum-curvature
    algorithm is used in most cases, the implementation varies
    sufficiently that no single algorithmic specification is available
    as a data transfer standard. Instead, the geometry of a RESQML
    wellbore trajectory is represented by a parametric line,
    parameterized by the MD. CRS and units of measure do not need to be
    consistent with the CRS and units of measure for wellbore trajectory
    representation.

    :ivar angle_uom: Defines the units of measure for the azimuth and
        inclination.
    :ivar angle_uom_custom_dict:
    :ivar azimuths: An array of azimuth angles, one for each survey
        station. The rotation is relative to the projected CRS north
        with a positive value indicating a clockwise rotation as seen
        from above. If the local CRS--whether in time or depth--is
        rotated relative to the projected CRS, then the azimuths remain
        relative to the projected CRS, not the local CRS. Note that the
        projection’s north is not the same as true north or magnetic
        north. A good definition of the different kinds of "north" can
        be found in the OGP Surveying &amp; Positioning Guidance Note 1
        http://www.ogp.org.uk/pubs/373-01.pdf (the "True, Grid and
        Magnetic North bearings" paragraph). BUSINESS RULE: Array length
        equals station count.
    :ivar first_station_location: XYZ location of the first station of
        the deviation survey.
    :ivar inclinations: Dip (or inclination) angle for each station.
        BUSINESS RULE: Array length equals station count.
    :ivar is_final: Used to indicate that this is a final version of the
        deviation survey, as distinct from the interim interpretations.
    :ivar mds: MD values for the position of the stations. BUSINESS
        RULE: Array length equals station count.
    :ivar md_uom: Units of measure of the measured depths along this
        deviation survey.
    :ivar md_uom_custom_dict:
    :ivar station_count: Number of stations.
    :ivar witsml_deviation_survey: A reference to an existing WITSML
        deviation survey.
    :ivar md_datum:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    angle_uom: Optional[Union[PlaneAngleUom, str]] = field(
        default=None,
        metadata={
            "name": "AngleUom",
            "type": "Element",
            "required": True,
            "pattern": r".*:.*",
        }
    )
    angle_uom_custom_dict: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "AngleUomCustomDict",
            "type": "Element",
        }
    )
    azimuths: Optional[AbstractFloatingPointArray] = field(
        default=None,
        metadata={
            "name": "Azimuths",
            "type": "Element",
            "required": True,
        }
    )
    first_station_location: Optional[SinglePointGeometry] = field(
        default=None,
        metadata={
            "name": "FirstStationLocation",
            "type": "Element",
            "required": True,
        }
    )
    inclinations: Optional[AbstractFloatingPointArray] = field(
        default=None,
        metadata={
            "name": "Inclinations",
            "type": "Element",
            "required": True,
        }
    )
    is_final: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsFinal",
            "type": "Element",
            "required": True,
        }
    )
    mds: Optional[AbstractFloatingPointArray] = field(
        default=None,
        metadata={
            "name": "Mds",
            "type": "Element",
            "required": True,
        }
    )
    md_uom: Optional[Union[LengthUom, str]] = field(
        default=None,
        metadata={
            "name": "MdUom",
            "type": "Element",
            "required": True,
            "pattern": r".*:.*",
        }
    )
    md_uom_custom_dict: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "MdUomCustomDict",
            "type": "Element",
        }
    )
    station_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "StationCount",
            "type": "Element",
            "required": True,
            "min_inclusive": 1,
        }
    )
    witsml_deviation_survey: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "WitsmlDeviationSurvey",
            "type": "Element",
        }
    )
    md_datum: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "MdDatum",
            "type": "Element",
            "required": True,
        }
    )
