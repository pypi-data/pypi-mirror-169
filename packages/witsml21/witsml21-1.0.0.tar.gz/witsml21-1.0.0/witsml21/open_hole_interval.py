from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.abstract_tvd_interval import AbstractTvdInterval
from witsml21.data_object_component_reference import DataObjectComponentReference
from witsml21.data_object_reference import DataObjectReference
from witsml21.event_info import EventInfo
from witsml21.extension_name_value import ExtensionNameValue
from witsml21.interval_status_history import IntervalStatusHistory
from witsml21.md_interval import MdInterval

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class OpenHoleInterval:
    """
    The location/interval of the open hole and its history.

    :ivar borehole_string: Reference to a borehole (the as-drilled hole
        through the earth).
    :ivar open_hole_md_interval: Openhole measured depth interval for
        this completion.
    :ivar open_hole_tvd_interval: Openhole true vertical depth interval
        for this completion.
    :ivar event_history: The OpenHoleInterval event information.
    :ivar geology_feature: Reference to a geology feature.
    :ivar geologic_unit_interpretation: Reference to a RESQML geologic
        unit interpretation.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar status_history:
    :ivar uid: Unique identifier for this instance of OpenHoleInterval.
    """
    borehole_string: Optional[DataObjectComponentReference] = field(
        default=None,
        metadata={
            "name": "BoreholeString",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    open_hole_md_interval: Optional[MdInterval] = field(
        default=None,
        metadata={
            "name": "OpenHoleMdInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    open_hole_tvd_interval: Optional[AbstractTvdInterval] = field(
        default=None,
        metadata={
            "name": "OpenHoleTvdInterval",
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
    status_history: List[IntervalStatusHistory] = field(
        default_factory=list,
        metadata={
            "name": "StatusHistory",
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
