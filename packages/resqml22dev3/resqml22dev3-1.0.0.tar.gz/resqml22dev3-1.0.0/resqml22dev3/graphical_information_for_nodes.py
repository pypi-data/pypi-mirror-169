from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from resqml22dev3.abstract_graphical_information_for_indexable_element import AbstractGraphicalInformationForIndexableElement
from resqml22dev3.display_space import DisplaySpace
from resqml22dev3.length_measure_ext import LengthMeasureExt
from resqml22dev3.node_symbol import NodeSymbol

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class GraphicalInformationForNodes(AbstractGraphicalInformationForIndexableElement):
    """
    To identify the space where the size has a meaning.

    :ivar constant_size: A size for all the nodes. Not defined if
        ActiveSizeInformationIndex is defined.
    :ivar display_space:
    :ivar show_symbol_every:
    :ivar symbol:
    """
    constant_size: Optional[LengthMeasureExt] = field(
        default=None,
        metadata={
            "name": "ConstantSize",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    display_space: Optional[DisplaySpace] = field(
        default=None,
        metadata={
            "name": "DisplaySpace",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    show_symbol_every: Optional[int] = field(
        default=None,
        metadata={
            "name": "ShowSymbolEvery",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    symbol: Optional[Union[NodeSymbol, str]] = field(
        default=None,
        metadata={
            "name": "Symbol",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "pattern": r".*:.*",
        }
    )
