from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.abstract_seismic_survey_feature import AbstractSeismicSurveyFeature
from resqml22dev3.integer_lattice_array import IntegerLatticeArray
from resqml22dev3.seismic_lattice_set_feature import SeismicLatticeSetFeature

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class SeismicLatticeFeature(AbstractSeismicSurveyFeature):
    """Defined by two lateral ordered dimensions: inline (lateral), crossline
    (lateral and orthogonal to the inline dimension), which are fixed.

    To specify its location, a seismic feature can be associated with
    the seismic coordinates of the points of a representation.
    Represented by a 2D grid representation.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    crossline_labels: Optional[IntegerLatticeArray] = field(
        default=None,
        metadata={
            "name": "CrosslineLabels",
            "type": "Element",
        }
    )
    is_part_of: Optional[SeismicLatticeSetFeature] = field(
        default=None,
        metadata={
            "name": "IsPartOf",
            "type": "Element",
        }
    )
    inline_labels: Optional[IntegerLatticeArray] = field(
        default=None,
        metadata={
            "name": "InlineLabels",
            "type": "Element",
        }
    )
