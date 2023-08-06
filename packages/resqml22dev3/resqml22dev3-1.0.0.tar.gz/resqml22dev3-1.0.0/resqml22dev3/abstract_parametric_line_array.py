from __future__ import annotations
from dataclasses import dataclass

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class AbstractParametricLineArray:
    """Defines an array of parametric lines.

    The array size is obtained from context. In the current schema, this may be as simple as a 1D array (#Lines=count) or a 2D array #Lines = NIL x NJL for an IJK grid representation.
    """
