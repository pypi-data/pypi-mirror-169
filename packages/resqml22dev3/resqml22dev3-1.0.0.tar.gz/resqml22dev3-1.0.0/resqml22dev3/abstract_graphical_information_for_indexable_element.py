from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.hsv_color import HsvColor

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class AbstractGraphicalInformationForIndexableElement:
    """
    :ivar active_alpha_information_index:
    :ivar active_annotation_information_index: Index into the graphical
        information set
    :ivar active_color_information_index: Index into the graphical
        information set
    :ivar active_size_information_index: Index into the graphical
        information set
    :ivar constant_alpha: It multiplies the opacity of the color map. If
        defined then AlphaInformation cannot be defined.
    :ivar is_visible:
    :ivar overwrite_color_alpha: If both ConstantAlpha and either
        ConstantColor or ColorInformation are defined, then setting this
        field to true will indicate that the ConstantAlpha must be used
        instead of the ConstantColor or ColorInformation alpha(s). Else
        the product of the two alpha should be used.
    :ivar constant_color:
    """
    active_alpha_information_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "ActiveAlphaInformationIndex",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    active_annotation_information_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "ActiveAnnotationInformationIndex",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    active_color_information_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "ActiveColorInformationIndex",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    active_size_information_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "ActiveSizeInformationIndex",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    constant_alpha: Optional[float] = field(
        default=None,
        metadata={
            "name": "ConstantAlpha",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    is_visible: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsVisible",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    overwrite_color_alpha: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OverwriteColorAlpha",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    constant_color: Optional[HsvColor] = field(
        default=None,
        metadata={
            "name": "ConstantColor",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
