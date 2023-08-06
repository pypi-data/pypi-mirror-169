from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.borehole import Borehole
from witsml21.data_object_reference import DataObjectReference
from witsml21.geology_feature import GeologyFeature
from witsml21.string_accessory import StringAccessory

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class BoreholeString:
    """A section of a borehole.

    Used to define the drilled hole that corresponds to the wellbore. A
    collection of contiguous and non-overlapping borehole sections is
    allowed. Each section has depth range, diameter, and kind.

    :ivar name: The name of the borehole string.
    :ivar borehole:
    :ivar geology_feature:
    :ivar accessories:
    :ivar reference_wellbore:
    :ivar uid: Unique identifier for this instance of BoreholeString.
    """
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    borehole: List[Borehole] = field(
        default_factory=list,
        metadata={
            "name": "Borehole",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    geology_feature: List[GeologyFeature] = field(
        default_factory=list,
        metadata={
            "name": "GeologyFeature",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    accessories: Optional[StringAccessory] = field(
        default=None,
        metadata={
            "name": "Accessories",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    reference_wellbore: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "ReferenceWellbore",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
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
