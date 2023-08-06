from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.abstract_interval import AbstractInterval
from witsml21.data_object_reference import DataObjectReference
from witsml21.pass_indexed_depth import PassIndexedDepth

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class PassIndexedDepthInterval(AbstractInterval):
    datum: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Datum",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    start: Optional[PassIndexedDepth] = field(
        default=None,
        metadata={
            "name": "Start",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    end: Optional[PassIndexedDepth] = field(
        default=None,
        metadata={
            "name": "End",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
