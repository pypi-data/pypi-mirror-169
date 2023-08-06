from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.abstract_string_array import AbstractStringArray

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class StringConstantArray(AbstractStringArray):
    """Represents an array of Boolean values where all values are identical.

    This an optimization for which an array of explicit Boolean values
    is not required.

    :ivar value: Value inside all the elements of the array.
    :ivar count: Size of the array.
    """
    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
            "max_length": 2000,
        }
    )
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
