from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from resqml22dev3.data_object_reference import DataObjectReference
from resqml22dev3.jagged_array import JaggedArray

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ConnectionInterpretations:
    """For each connection in the grid connection set representation, zero, one
    or more feature-interpretations.

    The use of a jagged array allows multiple interpretations for each
    connection, e.g., to represent multiple faults discretized onto a
    single connection. Note: Feature-interpretations are not restricted
    to faults, so that a connection may also represent a horizon or
    geobody boundary, for example.

    :ivar interpretation_indices: Indices for the interpretations for
        each connection, if any. The use of a RESQML jagged array allows
        zero or more than one interpretation to be associated with a
        single connection.
    :ivar feature_interpretation:
    """
    interpretation_indices: Optional[JaggedArray] = field(
        default=None,
        metadata={
            "name": "InterpretationIndices",
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
