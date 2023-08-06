from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional, Union
from xsdata.models.datatype import XmlDate
from resqml22dev3.abstract_object_type import AbstractObjectType
from resqml22dev3.actuate_value import ActuateValue
from resqml22dev3.anchor_definition import AnchorDefinition
from resqml22dev3.cartesian_cs_2 import CartesianCs2
from resqml22dev3.character_string_property_type import CharacterStringPropertyType
from resqml22dev3.conversion import Conversion
from resqml22dev3.ellipsoid_2 import Ellipsoid2
from resqml22dev3.ellipsoidal_cs_2 import EllipsoidalCs2
from resqml22dev3.ex_geographic_extent_property_type import ExGeographicExtentPropertyType
from resqml22dev3.ex_temporal_extent_property_type import ExTemporalExtentPropertyType
from resqml22dev3.identified_object_type import IdentifiedObjectType
from resqml22dev3.nil_reason_enumeration_value import NilReasonEnumerationValue
from resqml22dev3.prime_meridian_2 import PrimeMeridian2
from resqml22dev3.real_property_type import RealPropertyType
from resqml22dev3.show_value import ShowValue
from resqml22dev3.spherical_cs_2 import SphericalCs2
from resqml22dev3.vertical_cs_2 import VerticalCs2


@dataclass
class ExVerticalExtentType(AbstractObjectType):
    """
    Vertical domain of dataset.
    """
    class Meta:
        name = "EX_VerticalExtent_Type"
        target_namespace = "http://www.isotc211.org/2005/gmd"

    minimum_value: Optional[RealPropertyType] = field(
        default=None,
        metadata={
            "name": "minimumValue",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        }
    )
    maximum_value: Optional[RealPropertyType] = field(
        default=None,
        metadata={
            "name": "maximumValue",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        }
    )
    vertical_crs: Optional["ScCrsPropertyType"] = field(
        default=None,
        metadata={
            "name": "verticalCRS",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        }
    )


@dataclass
class ExVerticalExtent(ExVerticalExtentType):
    class Meta:
        name = "EX_VerticalExtent"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class ExVerticalExtentPropertyType:
    class Meta:
        name = "EX_VerticalExtent_PropertyType"
        target_namespace = "http://www.isotc211.org/2005/gmd"

    ex_vertical_extent: Optional[ExVerticalExtent] = field(
        default=None,
        metadata={
            "name": "EX_VerticalExtent",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    type: str = field(
        init=False,
        default="simple",
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    show: Optional[ShowValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    actuate: Optional[ActuateValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    uuidref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "namespace": "http://www.isotc211.org/2005/gco",
            "pattern": r"other:\w{2,}",
        }
    )


@dataclass
class ExExtentType(AbstractObjectType):
    """
    Information about spatial, vertical, and temporal extent.
    """
    class Meta:
        name = "EX_Extent_Type"
        target_namespace = "http://www.isotc211.org/2005/gmd"

    description: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    geographic_element: List[ExGeographicExtentPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "geographicElement",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    temporal_element: List[ExTemporalExtentPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "temporalElement",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    vertical_element: List[ExVerticalExtentPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "verticalElement",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )


@dataclass
class ExExtent(ExExtentType):
    class Meta:
        name = "EX_Extent"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class DomainOfValidity:
    """
    The gml:domainOfValidity property implements an association role to an
    EX_Extent object as encoded in ISO/TS 19139, either referencing or
    containing the definition of that extent.
    """
    class Meta:
        name = "domainOfValidity"
        namespace = "http://www.opengis.net/gml/3.2"

    ex_extent: Optional[ExExtent] = field(
        default=None,
        metadata={
            "name": "EX_Extent",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    type: str = field(
        init=False,
        default="simple",
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    show: Optional[ShowValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    actuate: Optional[ActuateValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:\w{2,}",
        }
    )


@dataclass
class AbstractCrstype(IdentifiedObjectType):
    class Meta:
        name = "AbstractCRSType"
        target_namespace = "http://www.opengis.net/gml/3.2"

    domain_of_validity: List[DomainOfValidity] = field(
        default_factory=list,
        metadata={
            "name": "domainOfValidity",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    scope: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "min_occurs": 1,
        }
    )


@dataclass
class AbstractDatumType(IdentifiedObjectType):
    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    domain_of_validity: Optional[DomainOfValidity] = field(
        default=None,
        metadata={
            "name": "domainOfValidity",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    scope: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "min_occurs": 1,
        }
    )
    anchor_definition: Optional[AnchorDefinition] = field(
        default=None,
        metadata={
            "name": "anchorDefinition",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    realization_epoch: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "realizationEpoch",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )


@dataclass
class AbstractGeneralDerivedCrstype(AbstractCrstype):
    class Meta:
        name = "AbstractGeneralDerivedCRSType"
        target_namespace = "http://www.opengis.net/gml/3.2"

    conversion: Optional[Conversion] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )


@dataclass
class GeodeticDatumType(AbstractDatumType):
    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    prime_meridian: Optional[PrimeMeridian2] = field(
        default=None,
        metadata={
            "name": "primeMeridian",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )
    ellipsoid: Optional[Ellipsoid2] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )


@dataclass
class VerticalDatumType(AbstractDatumType):
    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class GeodeticDatum1(GeodeticDatumType):
    """
    gml:GeodeticDatum is a geodetic datum defines the precise location and
    orientation in 3-dimensional space of a defined ellipsoid (or sphere), or
    of a Cartesian coordinate system centered in this ellipsoid (or sphere).
    """
    class Meta:
        name = "GeodeticDatum"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class VerticalDatum1(VerticalDatumType):
    """
    gml:VerticalDatum is a textual description and/or a set of parameters
    identifying a particular reference level surface used as a zero-height
    surface, including its position with respect to the Earth for any of the
    height types recognized by this International Standard.
    """
    class Meta:
        name = "VerticalDatum"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class GeodeticDatumPropertyType:
    """
    gml:GeodeticDatumPropertyType is a property type for association roles to a
    geodetic datum, either referencing or containing the definition of that
    datum.
    """
    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    geodetic_datum: Optional[GeodeticDatum1] = field(
        default=None,
        metadata={
            "name": "GeodeticDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    type: str = field(
        init=False,
        default="simple",
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    show: Optional[ShowValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    actuate: Optional[ActuateValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:\w{2,}",
        }
    )


@dataclass
class VerticalDatumPropertyType:
    """
    gml:VerticalDatumPropertyType is property type for association roles to a
    vertical datum, either referencing or containing the definition of that
    datum.
    """
    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    vertical_datum: Optional[VerticalDatum1] = field(
        default=None,
        metadata={
            "name": "VerticalDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    type: str = field(
        init=False,
        default="simple",
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    show: Optional[ShowValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    actuate: Optional[ActuateValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:\w{2,}",
        }
    )


@dataclass
class GeodeticDatum2(GeodeticDatumPropertyType):
    """
    gml:geodeticDatum is an association role to the geodetic datum used by this
    CRS.
    """
    class Meta:
        name = "geodeticDatum"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class VerticalDatum2(VerticalDatumPropertyType):
    """
    gml:verticalDatum is an association role to the vertical datum used by this
    CRS.
    """
    class Meta:
        name = "verticalDatum"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class GeodeticCrstype(AbstractCrstype):
    """
    gml:GeodeticCRS is a coordinate reference system based on a geodetic datum.
    """
    class Meta:
        name = "GeodeticCRSType"
        target_namespace = "http://www.opengis.net/gml/3.2"

    ellipsoidal_cs: Optional[EllipsoidalCs2] = field(
        default=None,
        metadata={
            "name": "ellipsoidalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    cartesian_cs: Optional[CartesianCs2] = field(
        default=None,
        metadata={
            "name": "cartesianCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    spherical_cs: Optional[SphericalCs2] = field(
        default=None,
        metadata={
            "name": "sphericalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    geodetic_datum: Optional[GeodeticDatum2] = field(
        default=None,
        metadata={
            "name": "geodeticDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )


@dataclass
class VerticalCrstype(AbstractCrstype):
    class Meta:
        name = "VerticalCRSType"
        target_namespace = "http://www.opengis.net/gml/3.2"

    vertical_cs: Optional[VerticalCs2] = field(
        default=None,
        metadata={
            "name": "verticalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )
    vertical_datum: Optional[VerticalDatum2] = field(
        default=None,
        metadata={
            "name": "verticalDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )


@dataclass
class GeodeticCrs(GeodeticCrstype):
    class Meta:
        name = "GeodeticCRS"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class VerticalCrs(VerticalCrstype):
    """gml:VerticalCRS is a 1D coordinate reference system used for recording
    heights or depths.

    Vertical CRSs make use of the direction of gravity to define the
    concept of height or depth, but the relationship with gravity may
    not be straightforward. By implication, ellipsoidal heights (h)
    cannot be captured in a vertical coordinate reference system.
    Ellipsoidal heights cannot exist independently, but only as an
    inseparable part of a 3D coordinate tuple defined in a geographic 3D
    coordinate reference system.
    """
    class Meta:
        name = "VerticalCRS"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class GeodeticCrspropertyType:
    """
    gml:GeodeticCRSPropertyType is a property type for association roles to a
    geodetic coordinate reference system, either referencing or containing the
    definition of that reference system.
    """
    class Meta:
        name = "GeodeticCRSPropertyType"
        target_namespace = "http://www.opengis.net/gml/3.2"

    geodetic_crs: Optional[GeodeticCrs] = field(
        default=None,
        metadata={
            "name": "GeodeticCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    type: str = field(
        init=False,
        default="simple",
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    show: Optional[ShowValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    actuate: Optional[ActuateValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:\w{2,}",
        }
    )


@dataclass
class BaseGeodeticCrs(GeodeticCrspropertyType):
    """
    gml:baseGeodeticCRS is an association role to the geodetic coordinate
    reference system used by this projected CRS.
    """
    class Meta:
        name = "baseGeodeticCRS"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class ProjectedCrstype(AbstractGeneralDerivedCrstype):
    class Meta:
        name = "ProjectedCRSType"
        target_namespace = "http://www.opengis.net/gml/3.2"

    base_geodetic_crs: Optional[BaseGeodeticCrs] = field(
        default=None,
        metadata={
            "name": "baseGeodeticCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    cartesian_cs: Optional[CartesianCs2] = field(
        default=None,
        metadata={
            "name": "cartesianCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )


@dataclass
class ProjectedCrs(ProjectedCrstype):
    """gml:ProjectedCRS is a 2D coordinate reference system used to approximate
    the shape of the earth on a planar surface, but in such a way that the
    distortion that is inherent to the approximation is carefully controlled
    and known.

    Distortion correction is commonly applied to calculated bearings and
    distances to produce values that are a close match to actual field
    values.
    """
    class Meta:
        name = "ProjectedCRS"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class ScCrsPropertyType:
    class Meta:
        name = "SC_CRS_PropertyType"
        target_namespace = "http://www.isotc211.org/2005/gsr"

    vertical_crs: Optional[VerticalCrs] = field(
        default=None,
        metadata={
            "name": "VerticalCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    projected_crs: Optional[ProjectedCrs] = field(
        default=None,
        metadata={
            "name": "ProjectedCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    geodetic_crs: Optional[GeodeticCrs] = field(
        default=None,
        metadata={
            "name": "GeodeticCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    type: str = field(
        init=False,
        default="simple",
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    show: Optional[ShowValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    actuate: Optional[ActuateValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    uuidref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "namespace": "http://www.isotc211.org/2005/gco",
            "pattern": r"other:\w{2,}",
        }
    )
