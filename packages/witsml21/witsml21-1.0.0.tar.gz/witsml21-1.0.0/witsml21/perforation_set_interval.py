from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.abstract_tvd_interval import AbstractTvdInterval
from witsml21.data_object_component_reference import DataObjectComponentReference
from witsml21.data_object_reference import DataObjectReference
from witsml21.event_info import EventInfo
from witsml21.extension_name_value import ExtensionNameValue
from witsml21.md_interval import MdInterval
from witsml21.perforation_status_history import PerforationStatusHistory

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class PerforationSetInterval:
    """
    The location/interval of the perforation set and its history.

    :ivar perforation_set: Reference to a perforation set.
    :ivar perforation_set_md_interval: Overall measured depth interval
        for this perforation set.
    :ivar perforation_set_tvd_interval: Overall true vertical depth
        interval for this perforation set.
    :ivar event_history: The PerforationSetInterval event information.
    :ivar geology_feature: Reference to a geology feature.
    :ivar geologic_unit_interpretation: Reference to a RESQML geologic
        unit interpretation.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar perforation_status_history:
    :ivar uid: Unique identifier for this instance of
        PerforationSetInterval.
    """
    perforation_set: Optional[DataObjectComponentReference] = field(
        default=None,
        metadata={
            "name": "PerforationSet",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    perforation_set_md_interval: Optional[MdInterval] = field(
        default=None,
        metadata={
            "name": "PerforationSetMdInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    perforation_set_tvd_interval: Optional[AbstractTvdInterval] = field(
        default=None,
        metadata={
            "name": "PerforationSetTvdInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    event_history: Optional[EventInfo] = field(
        default=None,
        metadata={
            "name": "EventHistory",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    geology_feature: List[DataObjectComponentReference] = field(
        default_factory=list,
        metadata={
            "name": "GeologyFeature",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    geologic_unit_interpretation: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "GeologicUnitInterpretation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
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
    perforation_status_history: List[PerforationStatusHistory] = field(
        default_factory=list,
        metadata={
            "name": "PerforationStatusHistory",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
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
