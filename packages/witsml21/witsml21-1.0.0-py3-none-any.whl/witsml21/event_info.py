from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.event_ref_info import EventRefInfo
from witsml21.extension_name_value import ExtensionNameValue

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class EventInfo:
    """
    Event information type.

    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar begin_event:
    :ivar end_event:
    """
    extension_name_value: List[ExtensionNameValue] = field(
        default_factory=list,
        metadata={
            "name": "ExtensionNameValue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    begin_event: Optional[EventRefInfo] = field(
        default=None,
        metadata={
            "name": "BeginEvent",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    end_event: Optional[EventRefInfo] = field(
        default=None,
        metadata={
            "name": "EndEvent",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
