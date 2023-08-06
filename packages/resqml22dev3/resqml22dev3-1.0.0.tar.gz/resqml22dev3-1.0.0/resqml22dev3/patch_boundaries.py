from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from resqml22dev3.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class PatchBoundaries:
    """Defines the boundaries of an indexed patch.

    These boundaries are outer and inner rings.

    :ivar referenced_patch: The XML index of the referenced patch inside
        this representation.
    :ivar inner_ring:
    :ivar outer_ring:
    """
    referenced_patch: Optional[int] = field(
        default=None,
        metadata={
            "name": "ReferencedPatch",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
            "min_inclusive": 0,
        }
    )
    inner_ring: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "InnerRing",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    outer_ring: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "OuterRing",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
