from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from resqml22dev3.abstract_feature_interpretation import AbstractFeatureInterpretation
from resqml22dev3.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class WellboreInterpretationSet(AbstractFeatureInterpretation):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    wellbore_interpretation: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "WellboreInterpretation",
            "type": "Element",
        }
    )
