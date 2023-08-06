from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.abstract_graphical_information_for_indexable_element import AbstractGraphicalInformationForIndexableElement

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class GraphicalInformationForWholeObject(AbstractGraphicalInformationForIndexableElement):
    active_contour_line_set_information_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "ActiveContourLineSetInformationIndex",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    display_title: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DisplayTitle",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
