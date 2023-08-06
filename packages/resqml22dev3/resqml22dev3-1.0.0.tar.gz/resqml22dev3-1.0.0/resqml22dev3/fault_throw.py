from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional, Union
from resqml22dev3.abstract_time_interval import AbstractTimeInterval
from resqml22dev3.throw_kind import ThrowKind

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class FaultThrow:
    """
    Identifies the characteristic of the throw of a fault interpretation.
    """
    throw: List[Union[ThrowKind, str]] = field(
        default_factory=list,
        metadata={
            "name": "Throw",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "min_occurs": 1,
            "pattern": r".*:.*",
        }
    )
    has_occurred_during: Optional[AbstractTimeInterval] = field(
        default=None,
        metadata={
            "name": "HasOccurredDuring",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
