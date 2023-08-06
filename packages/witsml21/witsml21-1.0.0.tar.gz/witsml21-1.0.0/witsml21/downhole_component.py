from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.abstract_object import AbstractObject
from witsml21.borehole_string_set import BoreholeStringSet
from witsml21.data_object_reference import DataObjectReference
from witsml21.downhole_string import DownholeString
from witsml21.downhole_string_set import DownholeStringSet
from witsml21.equipment_set import EquipmentSet
from witsml21.perforation_sets import PerforationSets

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class DownholeComponent(AbstractObject):
    """
    General downhole equipment information.

    :ivar start_date: The date this equipment was installed.
    :ivar end_date: The date the equipment was removed.
    :ivar well_head:
    :ivar borehole_string_set:
    :ivar downhole_string_set:
    :ivar equipment_set:
    :ivar perforation_sets:
    :ivar well:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/witsmlv2"

    start_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Element",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    end_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "EndDate",
            "type": "Element",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    well_head: Optional[DownholeString] = field(
        default=None,
        metadata={
            "name": "WellHead",
            "type": "Element",
        }
    )
    borehole_string_set: Optional[BoreholeStringSet] = field(
        default=None,
        metadata={
            "name": "BoreholeStringSet",
            "type": "Element",
        }
    )
    downhole_string_set: Optional[DownholeStringSet] = field(
        default=None,
        metadata={
            "name": "DownholeStringSet",
            "type": "Element",
        }
    )
    equipment_set: Optional[EquipmentSet] = field(
        default=None,
        metadata={
            "name": "EquipmentSet",
            "type": "Element",
        }
    )
    perforation_sets: Optional[PerforationSets] = field(
        default=None,
        metadata={
            "name": "PerforationSets",
            "type": "Element",
        }
    )
    well: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Well",
            "type": "Element",
            "required": True,
        }
    )
