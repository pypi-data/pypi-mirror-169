from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional, Union
from resqml22dev3.abstract_graphical_information import AbstractGraphicalInformation
from resqml22dev3.abstract_graphical_information_for_indexable_element import AbstractGraphicalInformationForIndexableElement
from resqml22dev3.viewer_kind import ViewerKind

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class DefaultGraphicalInformation(AbstractGraphicalInformation):
    """
    Either for Feature, Interp or representation, marker.

    :ivar viewer_id: Use this especially to differentiate between two
        viewers of the same kind
    :ivar viewer_kind:
    :ivar indexable_element_info:
    """
    viewer_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ViewerId",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    viewer_kind: Optional[Union[ViewerKind, str]] = field(
        default=None,
        metadata={
            "name": "ViewerKind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
            "pattern": r".*:.*",
        }
    )
    indexable_element_info: List[AbstractGraphicalInformationForIndexableElement] = field(
        default_factory=list,
        metadata={
            "name": "IndexableElementInfo",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "min_occurs": 1,
        }
    )
