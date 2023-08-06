from __future__ import annotations
from dataclasses import dataclass
from resqml22dev3.geologic_unit_interpretation import GeologicUnitInterpretation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class GeobodyInterpretation(GeologicUnitInterpretation):
    """A volume of rock that is identified based on some specific attribute,
    like its mineral content or other physical characteristic.

    Unlike stratigraphic or phase units, there is no associated time or
    fluid content semantic.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
