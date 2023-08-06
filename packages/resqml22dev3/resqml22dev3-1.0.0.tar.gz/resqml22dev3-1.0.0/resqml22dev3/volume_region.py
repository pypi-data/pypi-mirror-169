from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from resqml22dev3.data_object_reference import DataObjectReference
from resqml22dev3.volume_shell import VolumeShell

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class VolumeRegion:
    """The volume within a shell or envelope.

    Known issue (2.0): This object should be considered a volume region patch. Specifically the indexable element kind = patch, despite not inheriting from a patch, with the patch index given by the contained element.
    The volume region must be considered as a patch in version 2.0 (even if now, this volume region is not literally inheriting from the patch class).

    :ivar patch_index: This patch index is used to enumerate the volume
        regions. Known issue (2.0): Patch Index should  inherit from
        patch, instead of being listed as a volume region element.
        Volume regions must be considered as a patch in version 2.0
        (even if now, this volume region is not literally inheriting
        from the patch class).
    :ivar internal_shells:
    :ivar external_shell:
    :ivar represents:
    """
    patch_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "PatchIndex",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
            "min_inclusive": 0,
        }
    )
    internal_shells: List[VolumeShell] = field(
        default_factory=list,
        metadata={
            "name": "InternalShells",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    external_shell: Optional[VolumeShell] = field(
        default=None,
        metadata={
            "name": "ExternalShell",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    represents: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Represents",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
