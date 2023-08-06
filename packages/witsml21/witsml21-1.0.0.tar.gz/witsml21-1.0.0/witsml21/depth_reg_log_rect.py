from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.depth_reg_rectangle import DepthRegRectangle
from witsml21.extension_name_value import ExtensionNameValue
from witsml21.log_rectangle_type import LogRectangleType

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class DepthRegLogRect:
    """
    A region of an image containing a log rectangle.

    :ivar type: A region of an image containing a log section image.
    :ivar name: The name of a rectangular section.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar position:
    :ivar uid: Unique identifier for the log section.
    """
    type: Optional[LogRectangleType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
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
    position: Optional[DepthRegRectangle] = field(
        default=None,
        metadata={
            "name": "Position",
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
