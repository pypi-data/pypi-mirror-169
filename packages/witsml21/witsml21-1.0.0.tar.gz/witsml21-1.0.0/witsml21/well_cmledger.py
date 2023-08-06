from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.abstract_event_extension import AbstractEventExtension
from witsml21.abstract_object import AbstractObject
from witsml21.data_object_reference import DataObjectReference
from witsml21.day_cost import DayCost
from witsml21.downhole_component_reference import DownholeComponentReference
from witsml21.drill_activity_code import DrillActivityCode
from witsml21.event_type import EventType
from witsml21.md_interval import MdInterval
from witsml21.participant import Participant
from witsml21.time_measure import TimeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class WellCmledger(AbstractObject):
    """
    Information regarding details of Jobs &amp; Events.

    :ivar parent_event: Parent event reference id.
    :ivar dtim_start: Date and time that activities started.
    :ivar dtim_end: Date and time that activities were completed.
    :ivar duration: The activity duration (commonly in hours).
    :ivar md_interval: Measured depth interval for this activity.
    :ivar event_order: Order number of event.
    :ivar rig: RigUtilization data object reference.
    :ivar activity_code: Activity code
    :ivar type: Comment on type of this event, either referring to a job
        type or an  activity type e.g. a safety meeting.
    :ivar is_plan: True if planned.
    :ivar work_order_id: Extension event for work order id.
    :ivar business_associate: Service company or business
    :ivar responsible_person: Name or information about person
        responsible who is implementing the service or job.
    :ivar contact: Contact name or person to get in touch with. Might
        not necessarily be the person responsible.
    :ivar nonproductive: True if event is not productive.
    :ivar trouble: True if event implies is in-trouble
    :ivar preventive_maintenance: True of event is for preventive
        maintenance
    :ivar unplanned: True if there is no planning infomation for this
        activity.
    :ivar phase: Phase (large activity classification) e.g. Drill
        Surface Hole.
    :ivar comment: Comment on this ledger
    :ivar description: Description of this ledger
    :ivar downhole_component_reference:
    :ivar event_extension:
    :ivar cost:
    :ivar participant:
    :ivar wellbore:
    :ivar event_type:
    """
    class Meta:
        name = "WellCMLedger"
        namespace = "http://www.energistics.org/energyml/data/witsmlv2"

    parent_event: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "ParentEvent",
            "type": "Element",
        }
    )
    dtim_start: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimStart",
            "type": "Element",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    dtim_end: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimEnd",
            "type": "Element",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    duration: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "Duration",
            "type": "Element",
        }
    )
    md_interval: Optional[MdInterval] = field(
        default=None,
        metadata={
            "name": "MdInterval",
            "type": "Element",
        }
    )
    event_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "EventOrder",
            "type": "Element",
        }
    )
    rig: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "Rig",
            "type": "Element",
        }
    )
    activity_code: Optional[DrillActivityCode] = field(
        default=None,
        metadata={
            "name": "ActivityCode",
            "type": "Element",
        }
    )
    type: Optional[EventType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
        }
    )
    is_plan: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsPlan",
            "type": "Element",
        }
    )
    work_order_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "WorkOrderID",
            "type": "Element",
            "max_length": 64,
        }
    )
    business_associate: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "BusinessAssociate",
            "type": "Element",
        }
    )
    responsible_person: Optional[str] = field(
        default=None,
        metadata={
            "name": "ResponsiblePerson",
            "type": "Element",
            "max_length": 64,
        }
    )
    contact: Optional[str] = field(
        default=None,
        metadata={
            "name": "Contact",
            "type": "Element",
            "max_length": 64,
        }
    )
    nonproductive: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Nonproductive",
            "type": "Element",
        }
    )
    trouble: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Trouble",
            "type": "Element",
        }
    )
    preventive_maintenance: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PreventiveMaintenance",
            "type": "Element",
        }
    )
    unplanned: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Unplanned",
            "type": "Element",
        }
    )
    phase: Optional[str] = field(
        default=None,
        metadata={
            "name": "Phase",
            "type": "Element",
            "max_length": 64,
        }
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "name": "Comment",
            "type": "Element",
            "max_length": 2000,
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "max_length": 2000,
        }
    )
    downhole_component_reference: Optional[DownholeComponentReference] = field(
        default=None,
        metadata={
            "name": "DownholeComponentReference",
            "type": "Element",
        }
    )
    event_extension: List[AbstractEventExtension] = field(
        default_factory=list,
        metadata={
            "name": "EventExtension",
            "type": "Element",
        }
    )
    cost: List[DayCost] = field(
        default_factory=list,
        metadata={
            "name": "Cost",
            "type": "Element",
        }
    )
    participant: Optional[Participant] = field(
        default=None,
        metadata={
            "name": "Participant",
            "type": "Element",
        }
    )
    wellbore: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Wellbore",
            "type": "Element",
            "required": True,
        }
    )
    event_type: Optional[EventType] = field(
        default=None,
        metadata={
            "name": "EventType",
            "type": "Element",
        }
    )
