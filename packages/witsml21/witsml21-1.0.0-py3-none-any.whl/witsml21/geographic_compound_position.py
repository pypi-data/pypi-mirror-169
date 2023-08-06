from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.abstract_compound_position import AbstractCompoundPosition
from witsml21.geographic_compound_crs import GeographicCompoundCrs

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class GeographicCompoundPosition(AbstractCompoundPosition):
    latitude: Optional[float] = field(
        default=None,
        metadata={
            "name": "Latitude",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    longitude: Optional[float] = field(
        default=None,
        metadata={
            "name": "Longitude",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    vertical_coordinate: Optional[float] = field(
        default=None,
        metadata={
            "name": "VerticalCoordinate",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    geographic_compound_crs: Optional[GeographicCompoundCrs] = field(
        default=None,
        metadata={
            "name": "GeographicCompoundCrs",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
