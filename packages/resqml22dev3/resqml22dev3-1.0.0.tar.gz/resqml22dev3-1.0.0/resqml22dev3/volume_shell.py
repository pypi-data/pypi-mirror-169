from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from resqml22dev3.oriented_macro_face import OrientedMacroFace

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class VolumeShell:
    """
    The shell or envelope of a structural, stratigraphic, or fluid unit.
    """
    shell_uid: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShellUid",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    macro_faces: List[OrientedMacroFace] = field(
        default_factory=list,
        metadata={
            "name": "MacroFaces",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "min_occurs": 1,
        }
    )
