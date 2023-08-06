from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.abstract_activity_parameter import AbstractActivityParameter

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class IntegerQuantityParameter(AbstractActivityParameter):
    """
    Parameter containing an integer value.

    :ivar value: Integer value
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
