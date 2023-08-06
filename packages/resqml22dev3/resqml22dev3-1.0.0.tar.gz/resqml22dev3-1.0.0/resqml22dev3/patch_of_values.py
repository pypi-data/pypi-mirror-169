from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.abstract_value_array import AbstractValueArray

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class PatchOfValues:
    """A patch of values.

    See also Patch.

    :ivar representation_patch_index: Patch index used to attach
        properties to a specific patch of the indexable elements.
    :ivar values: Values to be attached to the indexable elements.
    """
    representation_patch_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "RepresentationPatchIndex",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "min_inclusive": 0,
        }
    )
    values: Optional[AbstractValueArray] = field(
        default=None,
        metadata={
            "name": "Values",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
