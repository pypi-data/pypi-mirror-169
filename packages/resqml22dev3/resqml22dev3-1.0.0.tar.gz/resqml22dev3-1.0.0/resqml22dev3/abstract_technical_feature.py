from __future__ import annotations
from dataclasses import dataclass
from resqml22dev3.abstract_feature import AbstractFeature

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class AbstractTechnicalFeature(AbstractFeature):
    """Objects that exist by the action of humans.

    Examples include: wells and all they may contain, seismic surveys
    (surface, permanent water bottom), or injected fluid volumes.
    Because the decision to deploy such equipment is the result of
    studies or decisions by humans, technical features are usually not
    subject to the same kind of large changes in interpretation as
    geologic features. However, they are still subject to measurement
    error and other sources of uncertainty, and so still can be
    considered as subject to "interpretation".
    """
