from __future__ import annotations
from dataclasses import dataclass
from resqml22dev3.abstract_values_property import AbstractValuesProperty

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class BooleanProperty(AbstractValuesProperty):
    """Information specific to one Boolean property.

    Used to capture a choice between 2 and only 2 possible values/states
    for each indexable element of a data object, for example,
    identifying active cells of a grid..
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
