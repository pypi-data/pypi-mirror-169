from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.abstract_parameter_key import AbstractParameterKey
from resqml22dev3.time_index import TimeIndex

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class TimeIndexParameterKey(AbstractParameterKey):
    time_index: Optional[TimeIndex] = field(
        default=None,
        metadata={
            "name": "TimeIndex",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
