from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.abstract_growing_object import AbstractGrowingObject
from witsml21.md_interval import MdInterval

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class AbstractMdGrowingObject(AbstractGrowingObject):
    """
    A growing object where the parts are of type eml:AbstractMdGrowingPart or
    eml:AbstractMdIntervalGrowingPart.

    :ivar md_interval: The measured depth interval for the parts in this
        growing object. MdTop MUST equal the minimum measured depth of
        any part (interval). MdBase MUST equal the maximum measured
        depth of any part (interval). In an ETP store, the interval
        values are managed by the store. This MUST be specified when
        there are parts in the object, and it MUST NOT be specified when
        there are no parts in the object.
    """
    md_interval: Optional[MdInterval] = field(
        default=None,
        metadata={
            "name": "MdInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
        }
    )
