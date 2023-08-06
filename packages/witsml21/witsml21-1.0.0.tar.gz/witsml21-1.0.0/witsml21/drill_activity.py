from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.abstract_tvd_interval import AbstractTvdInterval
from witsml21.abstract_vertical_depth import AbstractVerticalDepth
from witsml21.data_object_reference import DataObjectReference
from witsml21.drill_activity_class_type import DrillActivityTypeType
from witsml21.drill_activity_code import DrillActivityCode
from witsml21.extension_name_value import ExtensionNameValue
from witsml21.item_state import ItemState
from witsml21.md_interval import MdInterval
from witsml21.measured_depth import MeasuredDepth
from witsml21.name_struct import NameStruct
from witsml21.state_detail_activity import StateDetailActivity
from witsml21.time_measure import TimeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class DrillActivity:
    """
    Operations Activity Component Schema.

    :ivar dtim_start: Date and time that activities started.
    :ivar proprietary_code:
    :ivar dtim_end: Date and time that activities ended.
    :ivar duration: The activity duration (commonly in hours).
    :ivar md: The measured depth to the drilling activity/operation.
    :ivar tvd: True vertical depth to the drilling activity/operation.
    :ivar phase: Phase refers to a large activity classification, e.g.,
        drill surface hole.
    :ivar activity_code: A code used to define rig activity.
    :ivar detail_activity: Custom string to further define an activity.
    :ivar type_activity_class: Classifier (planned, unplanned,
        downtime).
    :ivar activity_md_interval: Measured depth interval over which the
        activity was conducted.
    :ivar activity_tvd_interval: True vertical depth interval over which
        the activity was conducted.
    :ivar bit_md_interval: Range of bit measured depths over which the
        activity occurred.
    :ivar state: Finish, interrupted, failed, etc.
    :ivar state_detail_activity: The outcome of the detailed activity.
    :ivar operator: Pointer to a BusinessAssociate representing the
        operator.
    :ivar optimum: Is the activity optimum.? Values are "true" (or "1")
        and "false" (or "0").
    :ivar productive: Does activity bring closer to objective?  Values
        are "true" (or "1") and "false" (or "0").
    :ivar item_state: The item state for the data object.
    :ivar comments: Comments and remarks.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar bha_run: A pointer to the bhaRun object related to this
        activity
    :ivar tubular:
    :ivar uid: Unique identifier for this instance of DrillActivity.
    """
    dtim_start: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimStart",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    proprietary_code: List[NameStruct] = field(
        default_factory=list,
        metadata={
            "name": "ProprietaryCode",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    dtim_end: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimEnd",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    duration: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "Duration",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    md: Optional[MeasuredDepth] = field(
        default=None,
        metadata={
            "name": "Md",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    tvd: Optional[AbstractVerticalDepth] = field(
        default=None,
        metadata={
            "name": "Tvd",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    phase: Optional[str] = field(
        default=None,
        metadata={
            "name": "Phase",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    activity_code: Optional[DrillActivityCode] = field(
        default=None,
        metadata={
            "name": "ActivityCode",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    detail_activity: Optional[str] = field(
        default=None,
        metadata={
            "name": "DetailActivity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    type_activity_class: Optional[DrillActivityTypeType] = field(
        default=None,
        metadata={
            "name": "TypeActivityClass",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    activity_md_interval: Optional[MdInterval] = field(
        default=None,
        metadata={
            "name": "ActivityMdInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    activity_tvd_interval: Optional[AbstractTvdInterval] = field(
        default=None,
        metadata={
            "name": "ActivityTvdInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    bit_md_interval: Optional[MdInterval] = field(
        default=None,
        metadata={
            "name": "BitMdInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    state: Optional[str] = field(
        default=None,
        metadata={
            "name": "State",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    state_detail_activity: Optional[StateDetailActivity] = field(
        default=None,
        metadata={
            "name": "StateDetailActivity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    operator: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Operator",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    optimum: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Optimum",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    productive: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Productive",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    item_state: Optional[ItemState] = field(
        default=None,
        metadata={
            "name": "ItemState",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    comments: Optional[str] = field(
        default=None,
        metadata={
            "name": "Comments",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 2000,
        }
    )
    extension_name_value: List[ExtensionNameValue] = field(
        default_factory=list,
        metadata={
            "name": "ExtensionNameValue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    bha_run: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "BhaRun",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    tubular: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Tubular",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
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
