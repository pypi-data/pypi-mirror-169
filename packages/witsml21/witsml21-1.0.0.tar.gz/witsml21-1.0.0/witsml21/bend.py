from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.extension_name_value import ExtensionNameValue
from witsml21.length_measure import LengthMeasure
from witsml21.plane_angle_measure import PlaneAngleMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class Bend:
    """
    Tubular Bend Component Schema.

    :ivar angle: Angle of the bend.
    :ivar dist_bend_bot: Distance of the bend from the bottom of the
        component.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar uid: Unique identifier for this instance of Bend.
    """
    angle: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "Angle",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    dist_bend_bot: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "DistBendBot",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
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
    uid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 64,
        }
    )
