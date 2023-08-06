from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.abstract_representation import AbstractRepresentation
from resqml22dev3.line_role import LineRole
from resqml22dev3.node_patch import NodePatch

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class PolylineRepresentation(AbstractRepresentation):
    """A representation made up of a single polyline or "polygonal chain",
    which may be closed or not.

    Definition from Wikipedia (http://en.wikipedia.org/wiki/Piecewise_linear_curve):
    A polygonal chain, polygonal curve, polygonal path, or piecewise linear curve, is a connected series of line segments. More formally, a polygonal chain P is a curve specified by a sequence of points \\scriptstyle(A_1, A_2, \\dots, A_n) called its vertices so that the curve consists of the line segments connecting the consecutive vertices.
    In computer graphics a polygonal chain is called a polyline and is often used to approximate curved paths.
    BUSINESS RULE: To record a polyline the writer software must give the values of the geometry of each node in an order corresponding to the logical series of segments (edges). The geometry of a polyline must be a 1D array of points.
    A simple polygonal chain is one in which only consecutive (or the first and the last) segments intersect and only at their endpoints.
    A closed polygonal chain (isClosed=True) is one in which the first vertex coincides with the last one, or the first and the last vertices are connected by a line segment.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    line_role: Optional[LineRole] = field(
        default=None,
        metadata={
            "name": "LineRole",
            "type": "Element",
        }
    )
    is_closed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsClosed",
            "type": "Element",
            "required": True,
        }
    )
    node_patch: Optional[NodePatch] = field(
        default=None,
        metadata={
            "name": "NodePatch",
            "type": "Element",
            "required": True,
        }
    )
