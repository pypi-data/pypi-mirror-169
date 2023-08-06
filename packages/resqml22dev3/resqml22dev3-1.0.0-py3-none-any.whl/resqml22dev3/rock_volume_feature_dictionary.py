from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from resqml22dev3.abstract_object import AbstractObject
from resqml22dev3.rock_volume_feature import RockVolumeFeature

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class RockVolumeFeatureDictionary(AbstractObject):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    rock_volume_feature: List[RockVolumeFeature] = field(
        default_factory=list,
        metadata={
            "name": "RockVolumeFeature",
            "type": "Element",
            "min_occurs": 2,
        }
    )
