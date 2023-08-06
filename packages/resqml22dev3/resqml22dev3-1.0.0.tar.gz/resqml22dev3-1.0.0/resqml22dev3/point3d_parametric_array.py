from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.abstract_integer_array import AbstractIntegerArray
from resqml22dev3.abstract_parametric_line_array import AbstractParametricLineArray
from resqml22dev3.abstract_point3d_array import AbstractPoint3DArray
from resqml22dev3.abstract_value_array import AbstractValueArray

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class Point3DParametricArray(AbstractPoint3DArray):
    """
    A parametric specification of an array of XYZ points.

    :ivar parameters: A multi-dimensional array of parametric values
        that implicitly specifies an array of XYZ points. The parametric
        values provided in this data-object must be consistent with the
        parametric values specified in the referenced parametric line
        array. When constructing a column-layer grid geometry using
        parametric points, the array indexing follows the dimensionality
        of the coordinate lines x NKL, which is either a 2D or 3D array.
    :ivar parametric_line_indices: An optional array of indices that map
        from the array index to the index of the corresponding
        parametric line. If this information is known from context, then
        this array is not needed. For example, in either of these cases:
        (1) If the mapping from array index to parametric line is 1:1.
        (2) If the mapping has already been specified, as with the
        pillar Index from the column-layer geometry of a grid. For
        example, when constructing a column-layer grid geometry using
        parametric lines, the array indexing follows the dimensionality
        of the coordinate lines.
    :ivar truncated_line_indices: A 2D array of line indices for use
        with intersecting parametric lines. Each record consists of a
        single line index, which indicates the array line that uses this
        truncation information, followed by the parametric line indices
        for each of the points on that line. For a non-truncated line,
        the equivalent record repeats the array line index NKL+1 times.
        Size = (NKL+1) x truncatedLineCount
    :ivar parametric_lines:
    """
    class Meta:
        name = "Point3dParametricArray"

    parameters: Optional[AbstractValueArray] = field(
        default=None,
        metadata={
            "name": "Parameters",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    parametric_line_indices: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "ParametricLineIndices",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    truncated_line_indices: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "TruncatedLineIndices",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    parametric_lines: Optional[AbstractParametricLineArray] = field(
        default=None,
        metadata={
            "name": "ParametricLines",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
