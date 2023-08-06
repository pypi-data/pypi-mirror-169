from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class EventRefInfo:
    """
    Event reference information.

    :ivar event: The referencing eventledger event.
    :ivar event_date: Install/pull date.
    """
    event: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Event",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    event_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "EventDate",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
