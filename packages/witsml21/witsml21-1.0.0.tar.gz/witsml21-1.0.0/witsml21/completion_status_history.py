from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.completion_status import CompletionStatus
from witsml21.md_interval import MdInterval

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class CompletionStatusHistory:
    """
    Information on the collection of Completion StatusHistory.

    :ivar status: Completion status.
    :ivar start_date: The start date of the status.
    :ivar end_date: The end date of the status.
    :ivar perforation_md_interval: Measured depth interval between the
        top and the base of the perforations.
    :ivar comment: Comments or remarks on the status.
    :ivar uid: Unique identifier for this instance of
        CompletionStatusHistory.
    """
    status: Optional[CompletionStatus] = field(
        default=None,
        metadata={
            "name": "Status",
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
    perforation_md_interval: Optional[MdInterval] = field(
        default=None,
        metadata={
            "name": "PerforationMdInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
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
