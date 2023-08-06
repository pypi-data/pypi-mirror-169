from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from resqml22dev3.abstract_object import AbstractObject
from resqml22dev3.abstract_projected_crs import AbstractProjectedCrs
from resqml22dev3.abstract_vertical_crs import AbstractVerticalCrs
from resqml22dev3.axis_order2d import AxisOrder2D
from resqml22dev3.data_object_reference import DataObjectReference
from resqml22dev3.length_uom import LengthUom
from resqml22dev3.plane_angle_measure import PlaneAngleMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class AbstractLocal3DCrs(AbstractObject):
    """Defines a local 2D+1D coordinate reference system (CRS), by translation
    and rotation, whose origin is located at the (X,Y,Z) offset from the
    projected and vertical 2D+1D CRS. For specific business rules, see the
    attribute definitions. The units of measure in XY must be the same as the
    projected CRS. The units of measure of the third coordinate is determined
    in the depth or concrete type. ArealRotation is a plane angle. Defines a
    local 3D CRS, which is subject to the following restrictions:

    - The projected 2D CRS must have orthogonal axes.
    - The vertical 1D CRS must be chosen so that it is orthogonal to the plane defined by the projected 2D CRS.
    As a consequence of the definition:
    - The local CRS forms a Cartesian system of axes.
    - The local areal axes are in the plane of the projected system.
    - The local areal axes are orthogonal to each other.
    This 3D system is semantically equivalent to a compound CRS composed of a local 2D areal system and a local 1D vertical system.
    The labels associated with the axes on this local system are X, Y, Z or X, Y, T.
    The relative orientation of the local Y axis with respect to the local X axis is identical to that of the projected axes.

    :ivar yoffset: The Y offset of the origin of the local areal axes
        relative to the projected CRS origin. BUSINESS RULE: The value
        MUST represent the second axis of the coordinate system. The
        unit of measure is defined by the unit of measure for the
        projected 2D CRS.
    :ivar zoffset: The Z offset of the origin of the local vertical axis
        relative to the vertical CRS origin. According to CRS type
        (depth or time) it corresponds to the depth or time datum.
        BUSINESS RULE: The value MUST represent the third axis of the
        coordinate system. The unit of measure is defined by the unit of
        measure for the vertical CRS.
    :ivar areal_rotation: The rotation of the local Y axis relative to
        the projected Y axis. - A positive value indicates a clockwise
        rotation from the projected Y axis. - A negative value indicates
        a counter-clockwise rotation form the projected Y axis.
    :ivar projected_axis_order: Defines the coordinate system axis order
        of the global projected CRS when the projected CRS is an unknown
        CRS, else it must correspond to the axis order of the projected
        CRS.
    :ivar projected_uom_custom_dict: A reference to the dictionary where
        the projected UOM is defined.
    :ivar projected_uom: Unit of measure of the associated projected
        CRS. BUSINESS RULE: When the projected CRS is well known, it
        must have the same UOM as the UOM defined by the well-known
        projected CRS. Explanation: A well-known CRS already defines the
        UOM. When you indicate that you use a CRS EPSG code, e.g., 7500,
        if you go to the EPSG database, you find the constrained UOM.
        This approach removes the need to depend on an EPSG database (or
        other external database), so RESQML copies the UOM of the well-
        known CRS into the RESQML CRS.
    :ivar vertical_uom: Unit of measure of the associated vertical CRS.
        BUSINESS RULE: When the vertical CRS is well known, it must have
        the same UOM defined by the well-known vertical CRS.
        Explanation: See ProjectedUom.
    :ivar vertical_uom_custom_dict: A reference to the dictionary where
        the vertical UOM is defined.
    :ivar zincreasing_downward: Indicates that Z values correspond to
        depth values and are increasing downward, as opposite to
        elevation values increasing upward. BUSINESS RULE: When the
        vertical CRS is already defined somewhere else (e.g., in a well-
        known source), it must correspond to the axis orientation of the
        vertical CRS.
    :ivar xoffset: The X location of the origin of the local areal axes
        relative to the projected CRS origin. BUSINESS RULE: The value
        MUST represent the first axis of the coordinate system. The unit
        of measure is defined by the unit of measure for the projected
        2D CRS.
    :ivar projected_crs:
    :ivar vertical_crs:
    """
    class Meta:
        name = "AbstractLocal3dCrs"

    yoffset: Optional[float] = field(
        default=None,
        metadata={
            "name": "YOffset",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    zoffset: Optional[float] = field(
        default=None,
        metadata={
            "name": "ZOffset",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    areal_rotation: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "ArealRotation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    projected_axis_order: Optional[AxisOrder2D] = field(
        default=None,
        metadata={
            "name": "ProjectedAxisOrder",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    projected_uom_custom_dict: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "ProjectedUomCustomDict",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    projected_uom: Optional[Union[LengthUom, str]] = field(
        default=None,
        metadata={
            "name": "ProjectedUom",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
            "pattern": r".*:.*",
        }
    )
    vertical_uom: Optional[Union[LengthUom, str]] = field(
        default=None,
        metadata={
            "name": "VerticalUom",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
            "pattern": r".*:.*",
        }
    )
    vertical_uom_custom_dict: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "VerticalUomCustomDict",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    zincreasing_downward: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ZIncreasingDownward",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    xoffset: Optional[float] = field(
        default=None,
        metadata={
            "name": "XOffset",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    projected_crs: Optional[AbstractProjectedCrs] = field(
        default=None,
        metadata={
            "name": "ProjectedCrs",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    vertical_crs: Optional[AbstractVerticalCrs] = field(
        default=None,
        metadata={
            "name": "VerticalCrs",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
