from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.abstract_growing_object_part import AbstractGrowingObjectPart
from witsml21.date_time_interval import DateTimeInterval

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class AbstractTimeIntervalGrowingPart(AbstractGrowingObjectPart):
    """
    :ivar time_interval: STORE MANAGED. This is populated by a store on
        read. Customer provided values are ignored on write
    """
    time_interval: Optional[DateTimeInterval] = field(
        default=None,
        metadata={
            "name": "TimeInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
