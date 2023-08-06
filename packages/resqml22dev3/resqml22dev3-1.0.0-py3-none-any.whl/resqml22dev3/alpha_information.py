from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from resqml22dev3.abstract_graphical_information import AbstractGraphicalInformation
from resqml22dev3.min_max import MinMax

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class AlphaInformation(AbstractGraphicalInformation):
    """Used for continuous properties and property kinds and for geometry.

    In the latter case, we need to point to the representation.

    :ivar alpha: Count equals to entry count. It multiplies the opacity
        of the color map.
    :ivar index: Count equals to opacity count.
    :ivar min_max:
    :ivar overwrite_color_alpha: If both Alpha and either ConstantColor
        or ColorInformation are defined, then setting this field to true
        will indicate that the Alpha must be used instead of the
        ConstantColor or ColorInformation alpha(s). Else the product of
        the two alpha should be used.
    :ivar use_logarithmic_mapping: Indicates that the log of the
        property values are taken into account when mapped with the
        index of the color map.
    :ivar use_reverse_mapping: Indicates that the minimum value of the
        property corresponds to the maximum index of the color map and
        that te maximum value of the property corresponds to the minimum
        index of the color map.
    :ivar value_vector_index: Especially useful for vector property and
        for geometry.
    """
    alpha: List[float] = field(
        default_factory=list,
        metadata={
            "name": "Alpha",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "min_occurs": 2,
        }
    )
    index: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Index",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "min_occurs": 2,
        }
    )
    min_max: Optional[MinMax] = field(
        default=None,
        metadata={
            "name": "MinMax",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    overwrite_color_alpha: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OverwriteColorAlpha",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    use_logarithmic_mapping: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UseLogarithmicMapping",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    use_reverse_mapping: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UseReverseMapping",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
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
