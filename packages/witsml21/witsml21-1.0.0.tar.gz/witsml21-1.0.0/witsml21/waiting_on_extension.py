from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.abstract_event_extension import AbstractEventExtension
from witsml21.extension_name_value import ExtensionNameValue

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class WaitingOnExtension(AbstractEventExtension):
    """
    Information on waiting event.

    :ivar sub_category: Sub category
    :ivar charge_type_code: Code for charge type
    :ivar business_org_waiting_on: Business organization waiting on
    :ivar is_no_charge_to_producer: Flag indicating whether producer is
        charged or not
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    """
    sub_category: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubCategory",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    charge_type_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChargeTypeCode",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    business_org_waiting_on: Optional[str] = field(
        default=None,
        metadata={
            "name": "BusinessOrgWaitingOn",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    is_no_charge_to_producer: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsNoChargeToProducer",
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
