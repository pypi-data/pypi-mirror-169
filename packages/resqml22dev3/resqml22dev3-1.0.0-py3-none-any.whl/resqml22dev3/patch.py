from __future__ import annotations
from dataclasses import dataclass

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class Patch:
    """A Patch is a mechanism in RESQML that provides a clear way of ordering
    indices to avoid ambiguity. For example, the representation of a horizon
    consists of 10 triangulated surfaces, to correctly represent the same
    horizon, the software importing or reading that horizon must know the
    indices within each of the 10 triangulated surfaces AND how the 10
    triangulated surfaces are sequenced. Representations with unique indexing
    of their elements DO NOT require Patches. For example, a (lower order)
    corner-point grid has an indexing scheme that can be defined without using
    Patches. However, a RESQML general purpose (GP) grid (an unconstrained
    hybrid of any of the other RESQML grid types) is much more complex and
    variable, with no "natural" sequence. For a reader to correctly interpret a
    GP grid, the software that created the GP grid must:

    - Explicitly define each Patch (specify the indices) that comprise the grid.
    - Designate the correct order of the Patches.
    If a representation includes indexable elements both specified within patches and external to patches, then Patch Index = 0 is defined to be the representation itself.
    For more information, see the RESQML Technical Usage Guide.
    """
