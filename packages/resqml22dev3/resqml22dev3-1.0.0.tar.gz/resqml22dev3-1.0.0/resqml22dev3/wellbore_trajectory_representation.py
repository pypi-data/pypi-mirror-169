from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from resqml22dev3.abstract_parametric_line_geometry import AbstractParametricLineGeometry
from resqml22dev3.abstract_representation import AbstractRepresentation
from resqml22dev3.data_object_reference import DataObjectReference
from resqml22dev3.length_uom import LengthUom
from resqml22dev3.md_domain import MdDomain
from resqml22dev3.wellbore_trajectory_parent_intersection import WellboreTrajectoryParentIntersection

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class WellboreTrajectoryRepresentation(AbstractRepresentation):
    """
    Representation of a wellbore trajectory.

    :ivar start_md: Specifies the measured depth  for the start of the
        wellbore trajectory. Range may often be from kickoff to TD, but
        this is not required. BUSINESS RULE: Start MD is always less
        than the Finish MD.
    :ivar finish_md: Specifies the ending measured depth of the range
        for the wellbore trajectory. Range may often be from kickoff to
        TD, but this is not required. BUSINESS RULE: Start MD is always
        less than the Finish MD.
    :ivar md_uom: Units of measure of the measured depths along this
        trajectory.
    :ivar custom_unit_dictionary:
    :ivar md_domain: Indicates if the MD is either in "driller" domain
        or "logger" domain.
    :ivar witsml_trajectory: Pointer to the WITSML trajectory that is
        contained in the referenced wellbore. (For information about
        WITSML well and wellbore references, see the definition for
        RESQML technical feature, WellboreFeature).
    :ivar parent_intersection:
    :ivar md_datum:
    :ivar deviation_survey:
    :ivar geometry: Explicit geometry is not required for vertical wells
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    start_md: Optional[float] = field(
        default=None,
        metadata={
            "name": "StartMd",
            "type": "Element",
            "required": True,
        }
    )
    finish_md: Optional[float] = field(
        default=None,
        metadata={
            "name": "FinishMd",
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
    custom_unit_dictionary: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "CustomUnitDictionary",
            "type": "Element",
        }
    )
    md_domain: Optional[MdDomain] = field(
        default=None,
        metadata={
            "name": "MdDomain",
            "type": "Element",
        }
    )
    witsml_trajectory: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "WitsmlTrajectory",
            "type": "Element",
        }
    )
    parent_intersection: Optional[WellboreTrajectoryParentIntersection] = field(
        default=None,
        metadata={
            "name": "ParentIntersection",
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
    deviation_survey: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "DeviationSurvey",
            "type": "Element",
        }
    )
    geometry: Optional[AbstractParametricLineGeometry] = field(
        default=None,
        metadata={
            "name": "Geometry",
            "type": "Element",
        }
    )
