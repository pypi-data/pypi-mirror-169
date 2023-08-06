from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.abstract_object import AbstractObject
from resqml22dev3.data_object_reference import DataObjectReference
from resqml22dev3.fluid_contact import FluidContact
from resqml22dev3.fluid_marker import FluidMarker
from resqml22dev3.geologic_boundary_kind import GeologicBoundaryKind

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class WellboreMarker(AbstractObject):
    """Representation of a wellbore marker that is located along a wellbore
    trajectory, one for each MD value in the wellbore frame.

    BUSINESS RULE: Ordering of the wellbore markers must match the
    ordering of the nodes in the wellbore marker frame representation.

    :ivar fluid_contact:
    :ivar fluid_marker:
    :ivar geologic_boundary_kind:
    :ivar witsml_formation_marker: Optional WITSML wellbore reference of
        the well marker frame.
    :ivar interpretation:
    """
    fluid_contact: Optional[FluidContact] = field(
        default=None,
        metadata={
            "name": "FluidContact",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    fluid_marker: Optional[FluidMarker] = field(
        default=None,
        metadata={
            "name": "FluidMarker",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    geologic_boundary_kind: Optional[GeologicBoundaryKind] = field(
        default=None,
        metadata={
            "name": "GeologicBoundaryKind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    witsml_formation_marker: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "WitsmlFormationMarker",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    interpretation: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Interpretation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
