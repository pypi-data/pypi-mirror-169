from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.well_status import WellStatus

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class WellStatusPeriod:
    """
    This class is used to represent a period of time when a facility had a
    consistent WellStatus.

    :ivar status: The facility's status.
    :ivar start_date_time: The date and time when the status started.
    :ivar end_date_time: The date and time when the status ended.
    """
    status: Optional[WellStatus] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    start_date_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "StartDateTime",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    end_date_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "EndDateTime",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
