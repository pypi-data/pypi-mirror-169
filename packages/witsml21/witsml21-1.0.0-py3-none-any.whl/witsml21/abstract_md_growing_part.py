from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.abstract_growing_object_part import AbstractGrowingObjectPart
from witsml21.measured_depth import MeasuredDepth

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class AbstractMdGrowingPart(AbstractGrowingObjectPart):
    """
    :ivar md: The measured depth of this object growing part. STORE
        MANAGED. This is populated by a store on read. Customer provided
        values are ignored on write
    """
    md: Optional[MeasuredDepth] = field(
        default=None,
        metadata={
            "name": "Md",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
