from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from resqml22dev3.abstract_object import AbstractObject
from resqml22dev3.activation import Activation
from resqml22dev3.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class LocalGridSet(AbstractObject):
    """Used to activate and/or deactivate the specified children grids as local
    grids on their parents.

    Once activated, this object indicates that a child grid replaces
    local portions of the corresponding parent grid. Specifically,
    properties and/or geometry in the region of a parent window will be
    stored on both the parent and child grids, usually with differing
    spatial resolutions. The choice of whether non-null properties are
    stored on both grids, or only the child grid, is application
    specific. Parentage is inferred from the child grid construction.
    Without a grid set activation, the local grids are always active.
    Otherwise, the grid set activation is used to activate and/or
    deactivate the local grids in the set at specific times.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    activation: Optional[Activation] = field(
        default=None,
        metadata={
            "name": "Activation",
            "type": "Element",
        }
    )
    child_grid: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "ChildGrid",
            "type": "Element",
            "min_occurs": 1,
        }
    )
