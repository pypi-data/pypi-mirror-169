from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.abstract_object import AbstractObject
from witsml21.abstract_tvd_interval import AbstractTvdInterval
from witsml21.completion_status import CompletionStatus
from witsml21.completion_status_history import CompletionStatusHistory
from witsml21.contact_interval_set import ContactIntervalSet
from witsml21.data_object_reference import DataObjectReference
from witsml21.event_info import EventInfo
from witsml21.md_interval import MdInterval

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class WellboreCompletion(AbstractObject):
    """The transferrable class of the WellboreCompletion object.

    Each individual wellbore completion data object represents a
    completion (i.e., open to flow) interval along a wellbore. Meaning
    "this section of wellbore is open to flow".

    :ivar wellbore_completion_no: CompletionNo, etc. API14.
    :ivar wellbore_completion_alias: Preferred alias name.
    :ivar event_history: The WellboreCompletion event information.
    :ivar wellbore_completion_date: Completion date.
    :ivar suffix_api: API suffix.
    :ivar completion_md_interval: Overall measured depth interval for
        this wellbore completion.
    :ivar completion_tvd_interval: Overall true vertical depth interval
        for this wellbore completion.
    :ivar current_status: Status (active, planned, suspended, testing,
        etc.) of the wellbore completion
    :ivar status_date: Date for when the status was established.
    :ivar status_history:
    :ivar contact_interval_set:
    :ivar reference_wellbore:
    :ivar well_completion:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/witsmlv2"

    wellbore_completion_no: Optional[str] = field(
        default=None,
        metadata={
            "name": "WellboreCompletionNo",
            "type": "Element",
            "max_length": 64,
        }
    )
    wellbore_completion_alias: Optional[str] = field(
        default=None,
        metadata={
            "name": "WellboreCompletionAlias",
            "type": "Element",
            "max_length": 64,
        }
    )
    event_history: List[EventInfo] = field(
        default_factory=list,
        metadata={
            "name": "EventHistory",
            "type": "Element",
        }
    )
    wellbore_completion_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "WellboreCompletionDate",
            "type": "Element",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    suffix_api: Optional[str] = field(
        default=None,
        metadata={
            "name": "SuffixAPI",
            "type": "Element",
            "max_length": 64,
        }
    )
    completion_md_interval: Optional[MdInterval] = field(
        default=None,
        metadata={
            "name": "CompletionMdInterval",
            "type": "Element",
        }
    )
    completion_tvd_interval: Optional[AbstractTvdInterval] = field(
        default=None,
        metadata={
            "name": "CompletionTvdInterval",
            "type": "Element",
        }
    )
    current_status: Optional[CompletionStatus] = field(
        default=None,
        metadata={
            "name": "CurrentStatus",
            "type": "Element",
        }
    )
    status_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "StatusDate",
            "type": "Element",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    status_history: List[CompletionStatusHistory] = field(
        default_factory=list,
        metadata={
            "name": "StatusHistory",
            "type": "Element",
        }
    )
    contact_interval_set: Optional[ContactIntervalSet] = field(
        default=None,
        metadata={
            "name": "ContactIntervalSet",
            "type": "Element",
        }
    )
    reference_wellbore: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "ReferenceWellbore",
            "type": "Element",
            "required": True,
        }
    )
    well_completion: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "WellCompletion",
            "type": "Element",
        }
    )
