from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


class CellShape(Enum):
    """Used to indicate that all cells are of a uniform topology, i.e., have
    the same number of nodes per cell.

    This information is supplied by the RESQML writer to indicate the
    complexity of the grid geometry, as an aide to the RESQML reader. If
    a specific cell shape is not appropriate, then use polyhedral.
    BUSINESS RULE: Should be consistent with the actual geometry of the
    grid.

    :cvar TETRAHEDRAL: All grid cells are constrained to have only 4
        nodes/cell with 4 faces/cell, 3 nodes/face, 4 nodes/cell for all
        cells (degeneracy allowed).
    :cvar PYRAMIDAL: All grid cells are constrained to have only 5
        nodes/cell with 5 faces/cell, with 1 quadrilateral face and 4
        triangular faces.
    :cvar PRISM: All grid cells are constrained to have 6 nodes/cell
        with 5 faces/cell, with 3 quadrilateral faces and 2 non-adjacent
        triangular faces, as in a column layer grid with triangular
        columns.
    :cvar HEXAHEDRAL: All grid cells are constrained to have 8
        nodes/cell with 6 faces/cell, 4 nodes/face, 8 nodes/cell for all
        cells (degeneracy allowed). Equivalent to IJK grid cells.
    :cvar POLYHEDRAL: If the cell geometry is not of a more specific
        kind, use polyhedral.
    """
    TETRAHEDRAL = "tetrahedral"
    PYRAMIDAL = "pyramidal"
    PRISM = "prism"
    HEXAHEDRAL = "hexahedral"
    POLYHEDRAL = "polyhedral"
