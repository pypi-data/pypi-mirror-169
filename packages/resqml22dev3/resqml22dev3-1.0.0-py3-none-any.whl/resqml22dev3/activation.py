from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.abstract_integer_array import AbstractIntegerArray
from resqml22dev3.time_series import TimeSeries

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class Activation:
    """Used to activate and deactivate the referencing object at the times
    indicated.

    - If the activation object is not present, then the referencing object is always active.
    - If the activation object is present, then the referencing object is not active until activated.

    :ivar activation_toggle_indices: The index in the time series at
        which the state of the referencing object is changed. Toggle
        changes state from inactive to active, or toggle changes state
        from active to inactive.
    :ivar time_series:
    """
    activation_toggle_indices: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "ActivationToggleIndices",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    time_series: Optional[TimeSeries] = field(
        default=None,
        metadata={
            "name": "TimeSeries",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
