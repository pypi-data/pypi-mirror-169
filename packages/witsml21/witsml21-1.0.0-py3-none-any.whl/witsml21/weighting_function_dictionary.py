from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from witsml21.abstract_object import AbstractObject
from witsml21.weighting_function import WeightingFunction

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class WeightingFunctionDictionary(AbstractObject):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/witsmlv2"

    weighting_function: List[WeightingFunction] = field(
        default_factory=list,
        metadata={
            "name": "WeightingFunction",
            "type": "Element",
            "min_occurs": 2,
        }
    )
