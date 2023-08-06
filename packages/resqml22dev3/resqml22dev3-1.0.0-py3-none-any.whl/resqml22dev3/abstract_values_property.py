from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from resqml22dev3.abstract_property import AbstractProperty
from resqml22dev3.patch_of_values import PatchOfValues
from resqml22dev3.property_kind_facet import PropertyKindFacet

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class AbstractValuesProperty(AbstractProperty):
    """Base class for property values.

    Each derived element provides specific property values, including
    point property in support of geometries.
    """
    patch_of_values: List[PatchOfValues] = field(
        default_factory=list,
        metadata={
            "name": "PatchOfValues",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "min_occurs": 1,
        }
    )
    facet: List[PropertyKindFacet] = field(
        default_factory=list,
        metadata={
            "name": "Facet",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
