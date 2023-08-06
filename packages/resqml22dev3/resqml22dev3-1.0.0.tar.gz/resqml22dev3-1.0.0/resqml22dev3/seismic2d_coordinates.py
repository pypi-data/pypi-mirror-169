from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.abstract_floating_point_array import AbstractFloatingPointArray
from resqml22dev3.abstract_seismic_coordinates import AbstractSeismicCoordinates

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class Seismic2DCoordinates(AbstractSeismicCoordinates):
    """A group of 2D seismic coordinates that stores the 1-to-1 mapping between
    geometry patch coordinates (usually X, Y, Z) and trace or inter-trace
    positions on a seismic line.

    BUSINESS RULE: This patch must reference a geometry patch by its
    UUID.

    :ivar line_abscissa: The sequence of trace or inter-trace positions
        that correspond to the geometry coordinates. BUSINESS RULE: Both
        sequences must be in the same order.
    :ivar vertical_coordinates: The sequence of vertical sample or
        inter-sample positions that corresponds to the geometry
        coordinates. BUSINESS RULE: Sequence must be in the same order
        as the previous one.
    """
    class Meta:
        name = "Seismic2dCoordinates"

    line_abscissa: Optional[AbstractFloatingPointArray] = field(
        default=None,
        metadata={
            "name": "LineAbscissa",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    vertical_coordinates: Optional[AbstractFloatingPointArray] = field(
        default=None,
        metadata={
            "name": "VerticalCoordinates",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
