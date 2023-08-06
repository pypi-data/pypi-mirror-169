from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.abstract_position import AbstractPosition
from witsml21.osduspatial_location_integration import OsduspatialLocationIntegration

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class BottomHoleLocation:
    """
    This class is used to represent the bottomhole location of a wellbore.

    :ivar location: The bottomhole's position.
    :ivar osdulocation_metadata: Additional OSDU-specific metadata about
        the location.
    """
    location: Optional[AbstractPosition] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    osdulocation_metadata: Optional[OsduspatialLocationIntegration] = field(
        default=None,
        metadata={
            "name": "OSDULocationMetadata",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
