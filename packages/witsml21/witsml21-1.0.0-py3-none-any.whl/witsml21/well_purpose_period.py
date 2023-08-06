from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.well_purpose import WellPurpose

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class WellPurposePeriod:
    """
    This class is used to represent a period of time when a facility had a
    consistent WellPurpose.

    :ivar purpose: The facility's purpose.
    :ivar start_date_time: The date and time when the purpose started.
    :ivar end_date_time: The date and time when the purpose ended.
    """
    purpose: Optional[WellPurpose] = field(
        default=None,
        metadata={
            "name": "Purpose",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    start_date_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "StartDateTime",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    end_date_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "EndDateTime",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
