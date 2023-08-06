from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.abstract3d_position import Abstract3DPosition
from witsml21.extension_name_value import ExtensionNameValue
from witsml21.length_measure import LengthMeasure
from witsml21.plane_angle_measure import PlaneAngleMeasure
from witsml21.target_section_scope import TargetSectionScope

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class TargetSection:
    """
    WITSML Element Types.

    :ivar sect_number: Sequence number of section, 1,2,3.
    :ivar type_target_section_scope: Section scope: Line or Arc.
    :ivar len_radius: Length of straight line section or radius of arc
        for continuous curve section.
    :ivar angle_arc: Direction of straight line section or radius of arc
        for continuous curve section.
    :ivar thick_above: Height of target above center point at the start
        of the section. In the case of an arc, the thickness above
        should vary linearly with the arc length.
    :ivar thick_below: Depth of target below center point at the start
        of the section. In the case of an arc, the thickness below
        should vary linearly with the arc length.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar location:
    :ivar uid:
    """
    sect_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "SectNumber",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    type_target_section_scope: Optional[TargetSectionScope] = field(
        default=None,
        metadata={
            "name": "TypeTargetSectionScope",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    len_radius: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "LenRadius",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    angle_arc: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "AngleArc",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    thick_above: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "ThickAbove",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    thick_below: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "ThickBelow",
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
    location: List[Abstract3DPosition] = field(
        default_factory=list,
        metadata={
            "name": "Location",
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
