from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from witsml21.abstract_object import AbstractObject
from witsml21.tool_error_model import ToolErrorModel

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class ToolErrorModelDictionary(AbstractObject):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/witsmlv2"

    tool_error_model: List[ToolErrorModel] = field(
        default_factory=list,
        metadata={
            "name": "ToolErrorModel",
            "type": "Element",
            "min_occurs": 2,
        }
    )
