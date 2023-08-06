from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.abstract_object import AbstractObject
from witsml21.data_object_reference import DataObjectReference
from witsml21.md_interval import MdInterval
from witsml21.wellbore_marker import WellboreMarker

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class WellboreMarkerSet(AbstractObject):
    """
    A collection of wellbore markers.

    :ivar marker_set_interval: Measured depth interval that contains the
        shallowest and deepest formation markers. This is computed by
        the server and is read only. STORE MANAGED. This is populated by
        a store on read. Customer provided values are ignored on write
    :ivar wellbore:
    :ivar formation_marker:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/witsmlv2"

    marker_set_interval: Optional[MdInterval] = field(
        default=None,
        metadata={
            "name": "MarkerSetInterval",
            "type": "Element",
            "required": True,
        }
    )
    wellbore: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Wellbore",
            "type": "Element",
        }
    )
    formation_marker: List[WellboreMarker] = field(
        default_factory=list,
        metadata={
            "name": "FormationMarker",
            "type": "Element",
        }
    )
