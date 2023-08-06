from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from witsml21.length_uom import LengthUom
from witsml21.time_uom import TimeUom
from witsml21.vertical_direction import VerticalDirection

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class VerticalAxis:
    """
    :ivar direction: Direction of the axis. Commonly used for values
        such as "easting, northing, depth, etc.."
    :ivar uom:
    :ivar is_time:
    """
    direction: Optional[VerticalDirection] = field(
        default=None,
        metadata={
            "name": "Direction",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    uom: Optional[Union[LengthUom, TimeUom, str]] = field(
        default=None,
        metadata={
            "name": "Uom",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
            "pattern": r".*:.*",
        }
    )
    is_time: bool = field(
        default=False,
        metadata={
            "name": "IsTime",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
