from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from witsml21.abstract_boolean_array import AbstractBooleanArray

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class BooleanXmlArray(AbstractBooleanArray):
    count_per_value: int = field(
        default=1,
        metadata={
            "name": "CountPerValue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    values: List[bool] = field(
        default_factory=list,
        metadata={
            "name": "Values",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
            "tokens": True,
        }
    )
