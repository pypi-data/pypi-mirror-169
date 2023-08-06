from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class AbstractOperatingRange:
    """
    :ivar comment:
    :ivar end_inclusive: Is the end inclusive or exclusive in the range.
    :ivar start_inclusive: Is the start inclusive or exclusive in the
        range.
    :ivar start:
    :ivar end:
    """
    comment: Optional[str] = field(
        default=None,
        metadata={
            "name": "Comment",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 2000,
        }
    )
    end_inclusive: Optional[bool] = field(
        default=None,
        metadata={
            "name": "EndInclusive",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    start_inclusive: Optional[bool] = field(
        default=None,
        metadata={
            "name": "StartInclusive",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    start: Optional[float] = field(
        default=None,
        metadata={
            "name": "Start",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    end: Optional[float] = field(
        default=None,
        metadata={
            "name": "End",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
