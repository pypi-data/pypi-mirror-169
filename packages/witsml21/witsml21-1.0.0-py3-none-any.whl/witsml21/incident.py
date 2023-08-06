from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.cost import Cost
from witsml21.data_object_reference import DataObjectReference
from witsml21.extension_name_value import ExtensionNameValue
from witsml21.time_measure import TimeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class Incident:
    """Operations HSE Schema.

    Captures data for a specific incident.

    :ivar dtim: Date and time the information is related to.
    :ivar reporter: Name of the person who prepared the incident report.
    :ivar num_minor_injury: Number of personnel with minor injuries.
    :ivar num_major_injury: Number of personnel with major injuries.
    :ivar num_fatality: Number of personnel killed due to the incident.
    :ivar is_near_miss: Near miss incident occurrence? Values are "true"
        (or "1") and "false" (or "0").
    :ivar desc_location: Location description.
    :ivar desc_accident: Accident description.
    :ivar remedial_action_desc: Remedial action description.
    :ivar cause_desc: Cause description.
    :ivar etim_lost_gross: Number of hours lost due to the incident.
    :ivar cost_loss_gross: Gross estimate of the cost incurred due to
        the incident.
    :ivar responsible_company: Pointer to a BusinessAssociate
        representing the company that caused the incident.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar uid: Unique identifier for this instance of Incident
    """
    dtim: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTim",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    reporter: Optional[str] = field(
        default=None,
        metadata={
            "name": "Reporter",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    num_minor_injury: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumMinorInjury",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    num_major_injury: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumMajorInjury",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    num_fatality: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumFatality",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    is_near_miss: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsNearMiss",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    desc_location: Optional[str] = field(
        default=None,
        metadata={
            "name": "DescLocation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    desc_accident: Optional[str] = field(
        default=None,
        metadata={
            "name": "DescAccident",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 2000,
        }
    )
    remedial_action_desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "RemedialActionDesc",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 2000,
        }
    )
    cause_desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "CauseDesc",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 2000,
        }
    )
    etim_lost_gross: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "ETimLostGross",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    cost_loss_gross: Optional[Cost] = field(
        default=None,
        metadata={
            "name": "CostLossGross",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    responsible_company: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "ResponsibleCompany",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
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
    uid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 64,
        }
    )
