from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from resqml22dev3.abstract_surface_framework_representation import AbstractSurfaceFrameworkRepresentation
from resqml22dev3.sealed_contact_representation_part import SealedContactRepresentationPart

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class SealedSurfaceFrameworkRepresentation(AbstractSurfaceFrameworkRepresentation):
    """A collection of contact representations parts, which are a list of
    contact patches and their identities.

    This collection of contact representations is completed by a set of
    representations gathered at the representation set representation
    level.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    sealed_contact_representation: List[SealedContactRepresentationPart] = field(
        default_factory=list,
        metadata={
            "name": "SealedContactRepresentation",
            "type": "Element",
        }
    )
