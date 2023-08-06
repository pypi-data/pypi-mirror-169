from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.abstract_grid_representation import AbstractGridRepresentation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class AbstractColumnLayerGridRepresentation(AbstractGridRepresentation):
    """Abstract class that includes IJK grids and unstructured column layer
    grids.

    All column layer grids have a layer index K=1,...,NK or
    K0=0,...,NK-1. Cell geometry is characterized by nodes on coordinate
    lines.

    :ivar nk: Number of layers in the grid. Must be positive.
    """
    nk: Optional[int] = field(
        default=None,
        metadata={
            "name": "Nk",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
            "min_inclusive": 1,
        }
    )
