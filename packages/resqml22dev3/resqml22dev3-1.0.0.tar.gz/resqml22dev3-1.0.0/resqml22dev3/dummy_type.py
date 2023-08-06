from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.custom_data import CustomData

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class DummyType:
    """This is a dummy type to make the generator create the correct import
    from Abstract.

    Do not use this for anything.
    """
    dummy_element: Optional[CustomData] = field(
        default=None,
        metadata={
            "name": "DummyElement",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
