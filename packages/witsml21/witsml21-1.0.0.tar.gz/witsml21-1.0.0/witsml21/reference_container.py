from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.component_reference import ComponentReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class ReferenceContainer:
    """
    Information on containing or contained components.

    :ivar string: DownholeString reference.
    :ivar equipment: Equipment reference.
    :ivar accesory_equipment: Reference to the equipment for this
        accessory.
    :ivar comment: Comment or remarks on this container reference.
    :ivar uid: Unique identifier for this instance of
        ReferenceContainer.
    """
    string: Optional[ComponentReference] = field(
        default=None,
        metadata={
            "name": "String",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    equipment: Optional[ComponentReference] = field(
        default=None,
        metadata={
            "name": "Equipment",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    accesory_equipment: Optional[ComponentReference] = field(
        default=None,
        metadata={
            "name": "AccesoryEquipment",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "name": "Comment",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "max_length": 2000,
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
