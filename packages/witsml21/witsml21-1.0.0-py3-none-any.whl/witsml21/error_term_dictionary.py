from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from witsml21.abstract_object import AbstractObject
from witsml21.error_term import ErrorTerm

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class ErrorTermDictionary(AbstractObject):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/witsmlv2"

    error_term: List[ErrorTerm] = field(
        default_factory=list,
        metadata={
            "name": "ErrorTerm",
            "type": "Element",
            "min_occurs": 2,
        }
    )
