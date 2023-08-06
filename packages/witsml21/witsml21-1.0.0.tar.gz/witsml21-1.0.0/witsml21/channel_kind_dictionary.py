from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from witsml21.abstract_object import AbstractObject
from witsml21.channel_kind import ChannelKind

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class ChannelKindDictionary(AbstractObject):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/witsmlv2"

    channel_kind: List[ChannelKind] = field(
        default_factory=list,
        metadata={
            "name": "ChannelKind",
            "type": "Element",
            "min_occurs": 1,
        }
    )
