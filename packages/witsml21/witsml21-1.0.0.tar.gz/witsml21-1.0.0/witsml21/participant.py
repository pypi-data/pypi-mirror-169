from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from witsml21.extension_name_value import ExtensionNameValue
from witsml21.member_object import MemberObject

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class Participant:
    """
    Information on WITSML objects used.

    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar participant:
    """
    extension_name_value: List[ExtensionNameValue] = field(
        default_factory=list,
        metadata={
            "name": "ExtensionNameValue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    participant: List[MemberObject] = field(
        default_factory=list,
        metadata={
            "name": "Participant",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
