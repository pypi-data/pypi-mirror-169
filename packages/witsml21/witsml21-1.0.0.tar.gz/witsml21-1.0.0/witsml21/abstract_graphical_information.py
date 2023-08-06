from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from witsml21.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class AbstractGraphicalInformation:
    target_object: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "TargetObject",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "min_occurs": 1,
        }
    )
