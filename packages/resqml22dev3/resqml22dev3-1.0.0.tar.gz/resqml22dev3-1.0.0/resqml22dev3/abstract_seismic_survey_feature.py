from __future__ import annotations
from dataclasses import dataclass
from resqml22dev3.abstract_technical_feature import AbstractTechnicalFeature

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class AbstractSeismicSurveyFeature(AbstractTechnicalFeature):
    """An organization of seismic lines. For the context of RESQML, a seismic
    survey does not refer to any vertical dimension information, but only
    areally at shot point locations or common midpoint gathers. The seismic
    traces, if needed by reservoir models, are transferred in an industry
    standard format such as SEGY. RESQML supports these basic types of seismic
    surveys:

    - seismic lattice (organization of the traces for the 3D acquisition and processing phases).
    - seismic line (organization of the traces for the 2D acquisition and processing phases).
    Additionally, these seismic lattices and seismic lines can be aggregated into sets.
    """
