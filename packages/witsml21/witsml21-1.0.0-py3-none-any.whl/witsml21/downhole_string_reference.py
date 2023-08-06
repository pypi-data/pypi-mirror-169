from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.component_reference import ComponentReference
from witsml21.data_object_component_reference import DataObjectComponentReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class DownholeStringReference:
    """
    Reference to a downhole string.

    :ivar downhole_string: Reference to a downhole string.
    :ivar string_equipment: Optional references to string equipment
        within the downhole string.
    """
    downhole_string: Optional[DataObjectComponentReference] = field(
        default=None,
        metadata={
            "name": "DownholeString",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    string_equipment: List[ComponentReference] = field(
        default_factory=list,
        metadata={
            "name": "StringEquipment",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
