from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


class IndexableElement(Enum):
    """Indexable elements for the different representations. The indexing of
    each element depends upon the specific representation. To order and
    reference the elements of a representation, RESQML makes extensive use of
    the concept of indexing. Both one-dimensional and multi-dimensional arrays
    of elements are used. So that all elements may be referenced in a
    consistent and uniform fashion, each multi-dimensional index must have a
    well-defined 1D index. Attributes below identify the IndexableElements,
    though not all elements apply to all types of representations. Indexable
    elements are used to:

    - attach geometry and properties to a representation.
    - identify portions of a representation when expressing a representation identity.
    - construct a sub-representation from an existing representation.
    For the table of indexable elements and the representations to which they apply, see the RESQML Technical Usage Guide.

    :cvar CELLS:
    :cvar INTERVALS_FROM_DATUM:
    :cvar COLUMN_EDGES:
    :cvar COLUMNS:
    :cvar CONTACTS:
    :cvar COORDINATE_LINES:
    :cvar EDGES:
    :cvar EDGES_PER_COLUMN:
    :cvar ENUMERATED_ELEMENTS:
    :cvar FACES:
    :cvar FACES_PER_CELL:
    :cvar INTERVAL_EDGES: Count = NKL (column-layer grids, only)
    :cvar INTERVALS:
    :cvar I0: Count = NI (IJK grids, only)
    :cvar I0_EDGES: Count = NIL (IJK grids, only)
    :cvar J0: Count = NJ (IJK grids, only)
    :cvar J0_EDGES: Count = NJL (IJK grids, only)
    :cvar LAYERS: Count = NK  (column-layer grids, only)
    :cvar LINES: Streamlines
    :cvar NODES:
    :cvar NODES_PER_CELL:
    :cvar NODES_PER_EDGE:
    :cvar NODES_PER_FACE:
    :cvar PATCHES:
    :cvar PILLARS:
    :cvar REGIONS:
    :cvar REPRESENTATION:
    :cvar SUBNODES:
    :cvar TRIANGLES:
    """
    CELLS = "cells"
    INTERVALS_FROM_DATUM = "intervals from datum"
    COLUMN_EDGES = "column edges"
    COLUMNS = "columns"
    CONTACTS = "contacts"
    COORDINATE_LINES = "coordinate lines"
    EDGES = "edges"
    EDGES_PER_COLUMN = "edges per column"
    ENUMERATED_ELEMENTS = "enumerated elements"
    FACES = "faces"
    FACES_PER_CELL = "faces per cell"
    INTERVAL_EDGES = "interval edges"
    INTERVALS = "intervals"
    I0 = "I0"
    I0_EDGES = "I0 edges"
    J0 = "J0"
    J0_EDGES = "J0 edges"
    LAYERS = "layers"
    LINES = "lines"
    NODES = "nodes"
    NODES_PER_CELL = "nodes per cell"
    NODES_PER_EDGE = "nodes per edge"
    NODES_PER_FACE = "nodes per face"
    PATCHES = "patches"
    PILLARS = "pillars"
    REGIONS = "regions"
    REPRESENTATION = "representation"
    SUBNODES = "subnodes"
    TRIANGLES = "triangles"
