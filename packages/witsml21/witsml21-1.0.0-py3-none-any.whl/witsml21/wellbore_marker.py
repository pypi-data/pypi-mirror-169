from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from witsml21.abstract_object import AbstractObject
from witsml21.abstract_vertical_depth import AbstractVerticalDepth
from witsml21.data_object_reference import DataObjectReference
from witsml21.geochronological_unit import GeochronologicalUnit
from witsml21.lithostratigraphic_unit import LithostratigraphicUnit
from witsml21.md_interval import MdInterval
from witsml21.measured_depth import MeasuredDepth
from witsml21.north_reference_kind import NorthReferenceKind
from witsml21.plane_angle_measure import PlaneAngleMeasure
from witsml21.stratigraphy_kind import StratigraphyKind
from witsml21.stratigraphy_kind_qualifier import StratigraphyKindQualifier
from witsml21.time_measure_ext import TimeMeasureExt
from witsml21.wellbore_marker_kind import WellboreMarkerKind
from witsml21.wellbore_point_of_interest import WellborePointOfInterest

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class WellboreMarker(AbstractObject):
    """Used to capture information about a geologic formation that was
    encountered in a wellbore.

    This object is uniquely identified within the context of one
    wellbore object.

    :ivar chronostratigraphic_top: The name of a geochronology for this
        marker, with the "kind" attribute specifying the
        geochronological time span.
    :ivar lithostratigraphic_top: Specifies the unit of
        lithostratigraphy.
    :ivar md: Logged measured depth at the top of marker. IMMUTABLE. Set
        on object creation and MUST NOT change thereafter. Customer
        provided changes after creation are an error. None of the sub-
        elements on the MarkerSetInterval can be changed,
    :ivar tvd: Logged true vertical depth at top of marker.
    :ivar dip_angle: Angle of dip with respect to horizontal. This is
        the true dip of the geologic surface, not the apparent dip
        measured locally by a tool.
    :ivar dip_direction: Interpreted downdip direction.
    :ivar dip_direction_ref: Specifies the definition of north. While
        this is optional because of legacy data, it is strongly
        recommended that this always be specified.
    :ivar observation_number: The observation number for this marker.
        This may be used, for example, to distinguish it from other
        marker observations recorded on the same date and/or with the
        same name.
    :ivar stratigraphy_kind: The kind of stratigraphy this marker
        represents. Should be populated if WellboreMarkerKind is
        stratigraphic.
    :ivar stratigraphy_kind_qualifier: An optional, additional qualifier
        on the kind of stratigraphy this marker represents.
    :ivar geologic_age: The geologic age associated with the marker.
    :ivar marker_qualifier: Qualifier for markers that may be missing or
        need additional information carried about them.
    :ivar point_of_interest: The point of interest in a wellbore that
        this marker represents. Should be populated if
        WellboreMarkerKind is point of interest.
    :ivar high_confidence_md_interval: Measured depth interval that
        marks the limit of the high confidence range for the marker
        pick.
    :ivar geologic_unit_interpretation: Reference to a RESQML geologic
        unit interpretation that this marker is characterizing.
    :ivar wellbore_marker_kind: A high level classification of what this
        marker represents: stratigraphic information, a point of
        interest in a well or something else.
    :ivar wellbore:
    :ivar trajectory:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/witsmlv2"

    chronostratigraphic_top: Optional[GeochronologicalUnit] = field(
        default=None,
        metadata={
            "name": "ChronostratigraphicTop",
            "type": "Element",
        }
    )
    lithostratigraphic_top: Optional[LithostratigraphicUnit] = field(
        default=None,
        metadata={
            "name": "LithostratigraphicTop",
            "type": "Element",
        }
    )
    md: Optional[MeasuredDepth] = field(
        default=None,
        metadata={
            "name": "Md",
            "type": "Element",
            "required": True,
        }
    )
    tvd: Optional[AbstractVerticalDepth] = field(
        default=None,
        metadata={
            "name": "Tvd",
            "type": "Element",
        }
    )
    dip_angle: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "DipAngle",
            "type": "Element",
        }
    )
    dip_direction: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "DipDirection",
            "type": "Element",
        }
    )
    dip_direction_ref: Optional[NorthReferenceKind] = field(
        default=None,
        metadata={
            "name": "DipDirectionRef",
            "type": "Element",
        }
    )
    observation_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "ObservationNumber",
            "type": "Element",
        }
    )
    stratigraphy_kind: Optional[Union[StratigraphyKind, str]] = field(
        default=None,
        metadata={
            "name": "StratigraphyKind",
            "type": "Element",
            "pattern": r".*:.*",
        }
    )
    stratigraphy_kind_qualifier: Optional[Union[StratigraphyKindQualifier, str]] = field(
        default=None,
        metadata={
            "name": "StratigraphyKindQualifier",
            "type": "Element",
            "pattern": r".*:.*",
        }
    )
    geologic_age: Optional[TimeMeasureExt] = field(
        default=None,
        metadata={
            "name": "GeologicAge",
            "type": "Element",
        }
    )
    marker_qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "MarkerQualifier",
            "type": "Element",
            "pattern": r".*:.*",
        }
    )
    point_of_interest: Optional[Union[WellborePointOfInterest, str]] = field(
        default=None,
        metadata={
            "name": "PointOfInterest",
            "type": "Element",
            "pattern": r".*:.*",
        }
    )
    high_confidence_md_interval: Optional[MdInterval] = field(
        default=None,
        metadata={
            "name": "HighConfidenceMdInterval",
            "type": "Element",
        }
    )
    geologic_unit_interpretation: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "GeologicUnitInterpretation",
            "type": "Element",
        }
    )
    wellbore_marker_kind: Optional[Union[WellboreMarkerKind, str]] = field(
        default=None,
        metadata={
            "name": "WellboreMarkerKind",
            "type": "Element",
            "pattern": r".*:.*",
        }
    )
    wellbore: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Wellbore",
            "type": "Element",
        }
    )
    trajectory: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Trajectory",
            "type": "Element",
        }
    )
