from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional, Union
from witsml21.abstract3d_position import Abstract3DPosition
from witsml21.abstract_object import AbstractObject
from witsml21.abstract_vertical_depth import AbstractVerticalDepth
from witsml21.data_object_reference import DataObjectReference
from witsml21.length_measure import LengthMeasure
from witsml21.north_reference_kind import NorthReferenceKind
from witsml21.plane_angle_measure import PlaneAngleMeasure
from witsml21.target_category import TargetCategory
from witsml21.target_scope import TargetScope
from witsml21.target_section import TargetSection

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class Target(AbstractObject):
    """The target object is used to capture information about intended targets
    of a trajectory survey.

    This object is uniquely identified within the context of one
    wellbore object.

    :ivar disp_ns_center: Northing of target center point in map
        coordinates.
    :ivar disp_ew_center: Easting of target center point in map
        coordinates.
    :ivar tvd: Vertical depth of the measurements.
    :ivar disp_ns_offset: North-south offset of target intercept point
        from shape center.
    :ivar disp_ew_offset: East-west offset of target intercept point
        from shape center.
    :ivar thick_above: Height of target above center point.
    :ivar thick_below: Depth of target below center point.
    :ivar dip: Angle of dip with respect to horizontal.
    :ivar strike: Direction of dip with respect to north azimuth
        reference.
    :ivar rotation: Direction of target geometry with respect to north
        azimuth reference.
    :ivar len_major_axis: Distance from center to perimeter in rotation
        direction. This may be ignored depending on the value of
        typeTargetScope.
    :ivar wid_minor_axis: Distance from center to perimeter at 90 deg to
        rotation direction. This may be ignored depending on the value
        of typeTargetScope.
    :ivar target_scope: The type of scope of the drilling target.
    :ivar disp_ns_sect_orig: Origin north-south used as starting point
        for sections, mandatory parameter when sections are used..
    :ivar disp_ew_sect_orig: Origin east-west used as starting point for
        sections, mandatory parameter when sections are used.
    :ivar azi_ref: Specifies the definition of north.
    :ivar cat_targ: Geological or drillers target.
    :ivar location:
    :ivar target_section:
    :ivar wellbore:
    :ivar parent_target:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/witsmlv2"

    disp_ns_center: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "DispNsCenter",
            "type": "Element",
        }
    )
    disp_ew_center: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "DispEwCenter",
            "type": "Element",
        }
    )
    tvd: Optional[AbstractVerticalDepth] = field(
        default=None,
        metadata={
            "name": "Tvd",
            "type": "Element",
        }
    )
    disp_ns_offset: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "DispNsOffset",
            "type": "Element",
        }
    )
    disp_ew_offset: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "DispEwOffset",
            "type": "Element",
        }
    )
    thick_above: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "ThickAbove",
            "type": "Element",
        }
    )
    thick_below: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "ThickBelow",
            "type": "Element",
        }
    )
    dip: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "Dip",
            "type": "Element",
        }
    )
    strike: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "Strike",
            "type": "Element",
        }
    )
    rotation: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "Rotation",
            "type": "Element",
        }
    )
    len_major_axis: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "LenMajorAxis",
            "type": "Element",
        }
    )
    wid_minor_axis: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "WidMinorAxis",
            "type": "Element",
        }
    )
    target_scope: Optional[Union[TargetScope, str]] = field(
        default=None,
        metadata={
            "name": "TargetScope",
            "type": "Element",
            "pattern": r".*:.*",
        }
    )
    disp_ns_sect_orig: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "DispNsSectOrig",
            "type": "Element",
        }
    )
    disp_ew_sect_orig: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "DispEwSectOrig",
            "type": "Element",
        }
    )
    azi_ref: Optional[NorthReferenceKind] = field(
        default=None,
        metadata={
            "name": "AziRef",
            "type": "Element",
        }
    )
    cat_targ: Optional[Union[TargetCategory, str]] = field(
        default=None,
        metadata={
            "name": "CatTarg",
            "type": "Element",
            "pattern": r".*:.*",
        }
    )
    location: List[Abstract3DPosition] = field(
        default_factory=list,
        metadata={
            "name": "Location",
            "type": "Element",
        }
    )
    target_section: List[TargetSection] = field(
        default_factory=list,
        metadata={
            "name": "TargetSection",
            "type": "Element",
        }
    )
    wellbore: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Wellbore",
            "type": "Element",
            "required": True,
        }
    )
    parent_target: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "ParentTarget",
            "type": "Element",
        }
    )
