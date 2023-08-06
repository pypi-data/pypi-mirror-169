from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.abstract_time_interval import AbstractTimeInterval
from resqml22dev3.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class GeneticBoundaryBasedTimeInterval(AbstractTimeInterval):
    """
    Geological time during which a geological event (e.g., deposition, erosion,
    fracturation, faulting, intrusion) occurred.
    """
    chrono_bottom: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "ChronoBottom",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    chrono_top: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "ChronoTop",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
