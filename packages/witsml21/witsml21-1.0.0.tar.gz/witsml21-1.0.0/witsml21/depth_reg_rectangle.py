from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.depth_reg_point import DepthRegPoint
from witsml21.extension_name_value import ExtensionNameValue

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class DepthRegRectangle:
    """Uses 4 corner points (Ul, Ur, Ll, Lr) to define the position (pixel) of
    a rectangular area of an image, using x-y coordinates.

    Most objects point to this object because most are rectangles, and
    use this schema to define each rectangle.

    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar ul: The upper left point of a rectangular region.
    :ivar ur: The upper right point of a rectangular region.
    :ivar ll: The lower left point of a rectangular region.
    :ivar lr: The lower right point of a rectangular region.
    :ivar uid: Unique identifier for the rectangular area.
    """
    extension_name_value: List[ExtensionNameValue] = field(
        default_factory=list,
        metadata={
            "name": "ExtensionNameValue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    ul: Optional[DepthRegPoint] = field(
        default=None,
        metadata={
            "name": "Ul",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    ur: Optional[DepthRegPoint] = field(
        default=None,
        metadata={
            "name": "Ur",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    ll: Optional[DepthRegPoint] = field(
        default=None,
        metadata={
            "name": "Ll",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    lr: Optional[DepthRegPoint] = field(
        default=None,
        metadata={
            "name": "Lr",
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
