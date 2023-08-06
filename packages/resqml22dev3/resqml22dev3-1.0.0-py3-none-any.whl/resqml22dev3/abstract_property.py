from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.abstract_integer_array import AbstractIntegerArray
from resqml22dev3.abstract_object import AbstractObject
from resqml22dev3.data_object_reference import DataObjectReference
from resqml22dev3.indexable_element import IndexableElement
from resqml22dev3.time_indices import TimeIndices

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class AbstractProperty(AbstractObject):
    """Base class for storing all property values on representations, except
    current geometry location.

    Values attached to a given element can be either a scalar or a
    vector. The size of the vector is constant on all elements, and it
    is assumed that all elements of the vector have identical property
    types and share the same unit of measure.

    :ivar indexable_element:
    :ivar realization_indices: Provide the list of indices corresponding
        to realizations number. For example, if a user wants to send the
        realization corresponding to p10, p20, ... he would write the
        array 10, 20, ... If not provided, then the realization count
        (which could be 1) does not introduce a dimension to the multi-
        dimensional array storage.
    :ivar value_count_per_indexable_element: Number of elements in a 1D
        list of properties of the same property kind. When used in a
        two-dimensional array, count is always the fastest. If not
        provided, then the value count does not introduce a dimension to
        the multi-dimensional array storage.
    :ivar property_kind: Pointer to a PropertyKind.  The Energistics
        dictionary can be found at
        http://w3.energistics.org/energyML/data/common/v2.1/ancillary/PropertyKindDictionary_v2.1.0.xml.
    :ivar time_indices:
    :ivar local_crs:
    :ivar supporting_representation:
    """
    indexable_element: Optional[IndexableElement] = field(
        default=None,
        metadata={
            "name": "IndexableElement",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    realization_indices: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "RealizationIndices",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    value_count_per_indexable_element: Optional[int] = field(
        default=None,
        metadata={
            "name": "ValueCountPerIndexableElement",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "min_inclusive": 1,
        }
    )
    property_kind: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "PropertyKind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    time_indices: Optional[TimeIndices] = field(
        default=None,
        metadata={
            "name": "TimeIndices",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    local_crs: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "LocalCrs",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    supporting_representation: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "SupportingRepresentation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
