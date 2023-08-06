from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.abstract_floating_point_array import AbstractFloatingPointArray
from resqml22dev3.correction_information import CorrectionInformation
from resqml22dev3.data_object_reference import DataObjectReference
from resqml22dev3.tvd_information import TvdInformation
from resqml22dev3.wellbore_frame_representation import WellboreFrameRepresentation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class SeismicWellboreFrameRepresentation(WellboreFrameRepresentation):
    """The interpretation of this representation must be a
    WellboreInterpretation.

    The acquisition information such as the time kind (e.g., TWT vs OWT
    for example) or survey acquisition type (e.g., checkshot vs VSP)
    should be captured by the associated acquisition activity.

    :ivar node_time_values: BUSINESS RULE: Count must be  equal to the
        inherited NodeCount. The direction of the supporting axis is
        given by the LocalTime3dCrs itself. It is necessary to get this
        information to know what means positive or negative values. The
        values are given with respect to the SeismicReferenceDatum. The
        UOM is the one specified in the LocalTime3dCrs.
    :ivar seismic_reference_datum: This is the Z value where the seismic
        time is equal to zero for this survey wellbore frame. The
        direction of the supporting axis is given by the LocalTime3dCrs
        of the associated wellbore trajectory. It is necessary to get
        the information to know what means a positive or a negative
        value. The value is given with respect to the ZOffset of the
        LocalDepth3dCrs of the associated wellbore trajectory. The UOM
        is the one specified in the LocalDepth3dCrs of the associated
        wellbore trajectory.
    :ivar weathering_velocity: The UOM is composed by: UOM of the
        LocalDepth3dCrs of the associated wellbore frame trajectory /
        UOM of the associated LocalTime3dCrs Sometimes also called
        seismic velocity replacement.
    :ivar tvd_information:
    :ivar correction_information:
    :ivar local_time3d_crs:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    node_time_values: Optional[AbstractFloatingPointArray] = field(
        default=None,
        metadata={
            "name": "NodeTimeValues",
            "type": "Element",
            "required": True,
        }
    )
    seismic_reference_datum: Optional[float] = field(
        default=None,
        metadata={
            "name": "SeismicReferenceDatum",
            "type": "Element",
            "required": True,
        }
    )
    weathering_velocity: Optional[float] = field(
        default=None,
        metadata={
            "name": "WeatheringVelocity",
            "type": "Element",
            "required": True,
        }
    )
    tvd_information: Optional[TvdInformation] = field(
        default=None,
        metadata={
            "name": "TvdInformation",
            "type": "Element",
        }
    )
    correction_information: Optional[CorrectionInformation] = field(
        default=None,
        metadata={
            "name": "CorrectionInformation",
            "type": "Element",
        }
    )
    local_time3d_crs: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "LocalTime3dCrs",
            "type": "Element",
            "required": True,
        }
    )
