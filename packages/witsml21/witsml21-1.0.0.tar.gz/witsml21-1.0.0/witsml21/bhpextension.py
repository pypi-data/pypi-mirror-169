from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.abstract_event_extension import AbstractEventExtension
from witsml21.extension_name_value import ExtensionNameValue

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class Bhpextension(AbstractEventExtension):
    """
    Information on bottom hole pressure during this event.

    :ivar bhpref_id: Reference to bottom hole pressure
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    """
    class Meta:
        name = "BHPExtension"

    bhpref_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "BHPRefID",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
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
