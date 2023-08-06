from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from resqml22dev3.abstract_integer_array import AbstractIntegerArray
from resqml22dev3.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class StreamlineWellbores:
    """Used to specify the wellbores on which streamlines may originate or
    terminate.

    Additional properties, e.g., MD, or cell index may be used to
    specify locations along a wellbore. The 0-based wellbore index is
    defined by the order of the wellbore in the list of
    WellboreTrajectoryRepresentation references.

    :ivar injector_per_line: Size of array = LineCount. Null values
        signify that that line does not initiate at an injector, e.g.,
        it may come from fluid expansion or an aquifer.
    :ivar producer_per_line: Size of array = LineCount Null values
        signify that that line does not terminate at a producer, e.g.,
        it may approach a stagnation area. BUSINESS RULE: The cell count
        must equal the number of non-null entries in this array.
    :ivar wellbore_trajectory_representation:
    """
    injector_per_line: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "InjectorPerLine",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    producer_per_line: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "ProducerPerLine",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    wellbore_trajectory_representation: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "WellboreTrajectoryRepresentation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "min_occurs": 1,
        }
    )
