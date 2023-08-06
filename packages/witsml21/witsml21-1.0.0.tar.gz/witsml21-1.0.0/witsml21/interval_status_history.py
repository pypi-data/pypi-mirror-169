from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.md_interval import MdInterval
from witsml21.physical_status import PhysicalStatus

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class IntervalStatusHistory:
    """
    Information on the status history in the interval.

    :ivar physical_status: The physical status of an interval (e.g.,
        open, closed, proposed).
    :ivar start_date: The start date of  the status and allocation
        factor.
    :ivar end_date: The end date of status and allocation factor.
    :ivar status_md_interval: Measured depth interval over which this
        status is valid for the given time frame.
    :ivar allocation_factor: Defines the proportional amount of fluid
        from the well completion that is flowing through this interval
        within a wellbore.
    :ivar comment: Comments and remarks about the interval over this
        period of time.
    :ivar uid: Unique identifier for this instance of
        IntervalStatusHistory.
    """
    physical_status: Optional[PhysicalStatus] = field(
        default=None,
        metadata={
            "name": "PhysicalStatus",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    start_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    end_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "EndDate",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    status_md_interval: Optional[MdInterval] = field(
        default=None,
        metadata={
            "name": "StatusMdInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    allocation_factor: Optional[str] = field(
        default=None,
        metadata={
            "name": "AllocationFactor",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+",
        }
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "name": "Comment",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 2000,
        }
    )
    uid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 64,
        }
    )
