from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class WellboreTrajectoryParentIntersection:
    """
    For a wellbore trajectory in a multi-lateral well, indicates the MD of the
    kickoff point where the trajectory begins and the corresponding MD of the
    parent trajectory.

    :ivar kickoff_md: KickoffMd is the measured depth for the start of
        the child trajectory, as defined within the child.
    :ivar parent_md: If the kickoff MD in the child (KickoffMd) is
        different from the kickoff MD in the parent (ParentMd), then
        specify the ParentMD here. If not specified, then these two MD's
        are implied to be identical.
    :ivar parent_trajectory:
    """
    kickoff_md: Optional[float] = field(
        default=None,
        metadata={
            "name": "KickoffMd",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    parent_md: Optional[float] = field(
        default=None,
        metadata={
            "name": "ParentMd",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    parent_trajectory: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "ParentTrajectory",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
