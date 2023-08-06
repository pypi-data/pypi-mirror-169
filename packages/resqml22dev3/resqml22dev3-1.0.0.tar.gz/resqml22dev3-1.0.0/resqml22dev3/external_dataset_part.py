from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class ExternalDatasetPart:
    """
    :ivar count:
    :ivar path_in_external_file: A string which is meaningful to the API
        which will store and retrieve data from the external file. For
        an HDF file this is the path of the referenced dataset in the
        external file. The separator between groups and final dataset is
        a slash '/' in an hdf file. For a LAS file this could be the
        list of mnemonics in the ~A block. For a SEG-Y file this could
        be a list of trace headers.
    :ivar start_index:
    :ivar epc_external_part_reference:
    """
    count: Optional[int] = field(
        default=None,
        metadata={
            "name": "Count",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
            "min_inclusive": 1,
        }
    )
    path_in_external_file: Optional[str] = field(
        default=None,
        metadata={
            "name": "PathInExternalFile",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
            "max_length": 2000,
        }
    )
    start_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "StartIndex",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
            "min_inclusive": 0,
        }
    )
    epc_external_part_reference: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "EpcExternalPartReference",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
