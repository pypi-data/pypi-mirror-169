from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from witsml21.abstract_object import AbstractObject
from witsml21.logging_tool_kind import LoggingToolKind

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class LoggingToolKindDictionary(AbstractObject):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/witsmlv2"

    logging_tool_kind: List[LoggingToolKind] = field(
        default_factory=list,
        metadata={
            "name": "LoggingToolKind",
            "type": "Element",
            "min_occurs": 1,
        }
    )
