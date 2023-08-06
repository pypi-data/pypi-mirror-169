from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.abstract_graphical_information import AbstractGraphicalInformation
from resqml22dev3.graphical_information_for_edges import GraphicalInformationForEdges

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ContourLineSetInformation(AbstractGraphicalInformation):
    display_label_on_major_line: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DisplayLabelOnMajorLine",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    display_label_on_minor_line: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DisplayLabelOnMinorLine",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    increment: Optional[float] = field(
        default=None,
        metadata={
            "name": "Increment",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    major_line_graphical_information: Optional[GraphicalInformationForEdges] = field(
        default=None,
        metadata={
            "name": "MajorLineGraphicalInformation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    minor_line_graphical_information: Optional[GraphicalInformationForEdges] = field(
        default=None,
        metadata={
            "name": "MinorLineGraphicalInformation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    show_major_line_every: Optional[int] = field(
        default=None,
        metadata={
            "name": "ShowMajorLineEvery",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    value_vector_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "ValueVectorIndex",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
