from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.abstract_event_extension import AbstractEventExtension
from witsml21.data_object_reference import DataObjectReference
from witsml21.extension_name_value import ExtensionNameValue

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class DownholeExtension(AbstractEventExtension):
    """
    Information on downhole related to this event.

    :ivar downhole_component: Reference to downhole component
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    """
    downhole_component: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "DownholeComponent",
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
