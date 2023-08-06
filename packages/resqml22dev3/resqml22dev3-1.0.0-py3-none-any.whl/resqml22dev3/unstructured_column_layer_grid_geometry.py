from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.abstract_boolean_array import AbstractBooleanArray
from resqml22dev3.abstract_column_layer_grid_geometry import AbstractColumnLayerGridGeometry
from resqml22dev3.column_shape import ColumnShape
from resqml22dev3.jagged_array import JaggedArray
from resqml22dev3.unstructured_column_edges import UnstructuredColumnEdges

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class UnstructuredColumnLayerGridGeometry(AbstractColumnLayerGridGeometry):
    """Description of the geometry of an unstructured column-layer grid, e.g.,
    parity and pinch, together with its supporting topology.

    Unstructured column-layer cell geometry is derived from column-layer
    cell geometry and hence is based upon nodes on coordinate lines.
    Geometry is contained within the representation of a grid.

    :ivar column_is_right_handed: List of columns that are right handed.
        Right handedness is evaluated following the pillar order and the
        K-direction tangent vector for each column.
    :ivar column_shape:
    :ivar pillar_count: Number of pillars in the grid. Must be positive.
        Pillars are used to describe the shape of the columns in the
        grid.
    :ivar pillars_per_column: List of pillars for each column. The
        pillars define the corners of each column. The number of pillars
        per column can be obtained from the offsets in the first list-
        of-lists array. BUSINESS RULE: The length of the first array in
        the list -of-lists construction must equal the columnCount.
    :ivar unstructured_column_edges:
    """
    column_is_right_handed: Optional[AbstractBooleanArray] = field(
        default=None,
        metadata={
            "name": "ColumnIsRightHanded",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    column_shape: Optional[ColumnShape] = field(
        default=None,
        metadata={
            "name": "ColumnShape",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    pillar_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "PillarCount",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
            "min_inclusive": 1,
        }
    )
    pillars_per_column: Optional[JaggedArray] = field(
        default=None,
        metadata={
            "name": "PillarsPerColumn",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    unstructured_column_edges: Optional[UnstructuredColumnEdges] = field(
        default=None,
        metadata={
            "name": "UnstructuredColumnEdges",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
