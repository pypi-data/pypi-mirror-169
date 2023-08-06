from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.abstract_event_extension import AbstractEventExtension
from witsml21.data_object_component_reference import DataObjectComponentReference
from witsml21.extension_name_value import ExtensionNameValue
from witsml21.perforating import Perforating

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class PerforatingExtension(AbstractEventExtension):
    """
    Information on the perforating event.

    :ivar perforation_set: The perforationSet reference.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar perforating:
    """
    perforation_set: Optional[DataObjectComponentReference] = field(
        default=None,
        metadata={
            "name": "PerforationSet",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
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
    perforating: List[Perforating] = field(
        default_factory=list,
        metadata={
            "name": "Perforating",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
