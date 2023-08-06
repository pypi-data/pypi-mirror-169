from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.abstract2d_position import Abstract2DPosition

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class AbstractCartesian2DPosition(Abstract2DPosition):
    """A 2D position given relative to either a projected or local engineering
    CRS.

    The meanings of the two coordinates and their units of measure are
    carried in the referenced CRS definition.
    """
    class Meta:
        name = "AbstractCartesian2dPosition"

    coordinate1: Optional[float] = field(
        default=None,
        metadata={
            "name": "Coordinate1",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    coordinate2: Optional[float] = field(
        default=None,
        metadata={
            "name": "Coordinate2",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
