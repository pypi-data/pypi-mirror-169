from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from witsml21.borehole_string_reference import BoreholeStringReference
from witsml21.data_object_component_reference import DataObjectComponentReference
from witsml21.downhole_string_reference import DownholeStringReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class DownholeComponentReference:
    """
    Reference to a downhole component identifier.

    :ivar string_equipment: Reference to string equipment
    :ivar perforation_set: Reference to perforation set
    :ivar borehole_string_reference:
    :ivar downhole_string_reference:
    """
    string_equipment: List[DataObjectComponentReference] = field(
        default_factory=list,
        metadata={
            "name": "StringEquipment",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    perforation_set: List[DataObjectComponentReference] = field(
        default_factory=list,
        metadata={
            "name": "PerforationSet",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    borehole_string_reference: List[BoreholeStringReference] = field(
        default_factory=list,
        metadata={
            "name": "BoreholeStringReference",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    downhole_string_reference: List[DownholeStringReference] = field(
        default_factory=list,
        metadata={
            "name": "DownholeStringReference",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
