from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.abstract_integer_array import AbstractIntegerArray

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class IntegerConstantArray(AbstractIntegerArray):
    """Represents an array of integer values where all values are identical.

    This an optimization for which an array of explicit integer values
    is not required.

    :ivar value: Values inside all the elements of the array.
    :ivar count: Size of the array.
    """
    value: Optional[int] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
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
