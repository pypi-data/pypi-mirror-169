from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from resqml22dev3.abstract_contact_representation_part import AbstractContactRepresentationPart
from resqml22dev3.abstract_surface_framework_representation import AbstractSurfaceFrameworkRepresentation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class NonSealedSurfaceFrameworkRepresentation(AbstractSurfaceFrameworkRepresentation):
    """A collection of contact representations parts, which are a list of
    contact patches with no identity.

    This collection of contact representations is completed by a set of
    representations gathered at the representation set representation
    level.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    non_sealed_contact_representation: List[AbstractContactRepresentationPart] = field(
        default_factory=list,
        metadata={
            "name": "NonSealedContactRepresentation",
            "type": "Element",
        }
    )
