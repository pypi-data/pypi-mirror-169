from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.abstract_tvd_interval import AbstractTvdInterval
from witsml21.borehole_type import BoreholeType
from witsml21.event_info import EventInfo
from witsml21.extension_name_value import ExtensionNameValue
from witsml21.length_measure import LengthMeasure
from witsml21.md_interval import MdInterval

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class Borehole:
    """
    Information on the borehole.

    :ivar name: The name of the borehole.
    :ivar type_borehole: Type of borehole. etc. cavern, cavity, normal
        borehole, under ream, etc.
    :ivar md_interval: Measured depth interval for the borehole.
    :ivar tvd_interval: True vertical depth interval for the borehole.
    :ivar borehole_diameter: Borehole diameter.
    :ivar description_permanent: The description of this equipment to be
        permanently kept.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar equipment_event_history:
    :ivar uid: Unique identifier for this instance of Borehole.
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
    type_borehole: Optional[BoreholeType] = field(
        default=None,
        metadata={
            "name": "TypeBorehole",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    md_interval: Optional[MdInterval] = field(
        default=None,
        metadata={
            "name": "MdInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    tvd_interval: Optional[AbstractTvdInterval] = field(
        default=None,
        metadata={
            "name": "TvdInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    borehole_diameter: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "BoreholeDiameter",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    description_permanent: Optional[str] = field(
        default=None,
        metadata={
            "name": "DescriptionPermanent",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 2000,
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
    equipment_event_history: Optional[EventInfo] = field(
        default=None,
        metadata={
            "name": "EquipmentEventHistory",
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
