from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.abstract_object import AbstractObject
from witsml21.active_status_kind import ActiveStatusKind

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class AbstractActiveObject(AbstractObject):
    """
    :ivar active_status: Describes the active status of the object,
        whether active or inactive. STORE MANAGED. This is populated by
        a store on read. Customer provided values are ignored on write
    """
    active_status: Optional[ActiveStatusKind] = field(
        default=None,
        metadata={
            "name": "ActiveStatus",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
