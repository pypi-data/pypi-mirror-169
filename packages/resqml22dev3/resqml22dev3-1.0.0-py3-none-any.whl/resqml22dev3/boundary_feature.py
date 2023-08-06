from __future__ import annotations
from dataclasses import dataclass
from resqml22dev3.abstract_feature import AbstractFeature

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class BoundaryFeature(AbstractFeature):
    """An interface between two objects, such as horizons and faults.

    It is a surface object. A RockVolumeFeature is a geological feature
    (which is the general concept that refers to the various categories
    of geological objects that exist in the natural world). For example:
    the stratigraphic boundaries, the =geobody boundaries or the fluid
    boundaries that are present before production. To simplify the
    hierarchy of concepts, the geological feature is not represented in
    the RESQML design.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
