from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from witsml21.downhole_string import DownholeString

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class DownholeStringSet:
    """
    Information on a collection of downhole strings.
    """
    downhole_string: List[DownholeString] = field(
        default_factory=list,
        metadata={
            "name": "DownholeString",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "min_occurs": 1,
        }
    )
