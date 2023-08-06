from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from resqml22dev3.abstract_floating_point_array import AbstractFloatingPointArray
from resqml22dev3.abstract_representation import AbstractRepresentation
from resqml22dev3.cell_fluid_phase_units import CellFluidPhaseUnits
from resqml22dev3.data_object_reference import DataObjectReference
from resqml22dev3.interval_stratigraphic_units import IntervalStratigraphicUnits

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class WellboreFrameRepresentation(AbstractRepresentation):
    """Representation of a wellbore that is organized along a wellbore
    trajectory by its MD values.

    RESQML uses MD values to associate properties on points and to
    organize association of properties on intervals between MD points.

    :ivar node_count: Number of nodes. Must be positive.
    :ivar node_md: MD values for each node. BUSINESS RULE: MD values and
        UOM must be consistent with the trajectory representation.
    :ivar witsml_log: The reference to the equivalent WITSML well log.
    :ivar trajectory:
    :ivar interval_stratigraphi_units:
    :ivar cell_fluid_phase_units:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    node_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "NodeCount",
            "type": "Element",
            "required": True,
            "min_inclusive": 1,
        }
    )
    node_md: Optional[AbstractFloatingPointArray] = field(
        default=None,
        metadata={
            "name": "NodeMd",
            "type": "Element",
            "required": True,
        }
    )
    witsml_log: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "WitsmlLog",
            "type": "Element",
        }
    )
    trajectory: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Trajectory",
            "type": "Element",
            "required": True,
        }
    )
    interval_stratigraphi_units: List[IntervalStratigraphicUnits] = field(
        default_factory=list,
        metadata={
            "name": "IntervalStratigraphiUnits",
            "type": "Element",
        }
    )
    cell_fluid_phase_units: Optional[CellFluidPhaseUnits] = field(
        default=None,
        metadata={
            "name": "CellFluidPhaseUnits",
            "type": "Element",
        }
    )
