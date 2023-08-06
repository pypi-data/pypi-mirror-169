from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.abstract_boolean_array import AbstractBooleanArray
from witsml21.abstract_integer_array import AbstractIntegerArray

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class IntegerArrayFromBooleanMaskArray(AbstractIntegerArray):
    """
    One-dimensional array of integer values obtained from the true elements of
    the Boolean mask.

    :ivar count_per_value:
    :ivar mask: Boolean mask. A true element indicates that the index is
        included on the list of integer values.
    """
    count_per_value: int = field(
        default=1,
        metadata={
            "name": "CountPerValue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    mask: Optional[AbstractBooleanArray] = field(
        default=None,
        metadata={
            "name": "Mask",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
