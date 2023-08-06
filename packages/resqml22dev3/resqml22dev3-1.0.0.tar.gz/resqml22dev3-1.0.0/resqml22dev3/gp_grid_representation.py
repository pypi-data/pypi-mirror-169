from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from resqml22dev3.abstract_grid_representation import AbstractGridRepresentation
from resqml22dev3.column_layer_gp_grid import ColumnLayerGpGrid
from resqml22dev3.unstructured_gp_grid_patch import UnstructuredGpGridPatch

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class GpGridRepresentation(AbstractGridRepresentation):
    """General purpose (GP) grid representation, which includes and/or extends
    the features from all other grid representations.

    This general purpose representation is included in the schema for
    research and/or advanced modeling purposes, but is not expected to
    be used for routine data transfer.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    unstructured_gp_grid_patch: List[UnstructuredGpGridPatch] = field(
        default_factory=list,
        metadata={
            "name": "UnstructuredGpGridPatch",
            "type": "Element",
        }
    )
    column_layer_gp_grid: List[ColumnLayerGpGrid] = field(
        default_factory=list,
        metadata={
            "name": "ColumnLayerGpGrid",
            "type": "Element",
        }
    )
