from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class TimestampedCommentString:
    """
    A timestamped textual description.

    :ivar value:
    :ivar d_tim: The timestamp of the time-qualified comment.
    """
    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 2000,
        }
    )
    d_tim: Optional[str] = field(
        default=None,
        metadata={
            "name": "dTim",
            "type": "Attribute",
            "required": True,
            "pattern": r".+T.+[Z+\-].*",
        }
    )
