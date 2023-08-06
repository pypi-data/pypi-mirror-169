from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from resqml22dev3.external_dataset_part import ExternalDatasetPart

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class ExternalDataset:
    external_file_proxy: List[ExternalDatasetPart] = field(
        default_factory=list,
        metadata={
            "name": "ExternalFileProxy",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "min_occurs": 1,
        }
    )
