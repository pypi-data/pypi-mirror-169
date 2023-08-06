from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from resqml22dev3.abstract_object import AbstractObject
from resqml22dev3.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class FeatureInterpretationSet(AbstractObject):
    """
    This class allows feature interpretations to be grouped together, mainly to
    specify the constituents of a StructuralOrganizationInterpretation.

    :ivar is_homogeneous: Indicates that all of the selected
        interpretations are of a single kind.
    :ivar feature_interpretation:
    """
    is_homogeneous: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsHomogeneous",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    feature_interpretation: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "FeatureInterpretation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "min_occurs": 1,
        }
    )
