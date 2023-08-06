from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.abstract_reference_point import AbstractReferencePoint
from witsml21.data_object_reference import DataObjectReference
from witsml21.horizontal_coordinates import HorizontalCoordinates

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class RecursiveReferencePoint(AbstractReferencePoint):
    """
    A reference point defined in the context of another reference point.

    :ivar vertical_coordinate: The vertical distance in elevation
        (positive up) between the reference point and its
        BaseReferencePoint.
    :ivar horizontal_coordinates:
    :ivar base_reference_point:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/commonv2"

    vertical_coordinate: Optional[float] = field(
        default=None,
        metadata={
            "name": "VerticalCoordinate",
            "type": "Element",
        }
    )
    horizontal_coordinates: Optional[HorizontalCoordinates] = field(
        default=None,
        metadata={
            "name": "HorizontalCoordinates",
            "type": "Element",
        }
    )
    base_reference_point: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "BaseReferencePoint",
            "type": "Element",
            "required": True,
        }
    )
