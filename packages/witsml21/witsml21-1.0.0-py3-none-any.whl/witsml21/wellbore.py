from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional, Union
from witsml21.abstract_active_object import AbstractActiveObject
from witsml21.abstract_vertical_depth import AbstractVerticalDepth
from witsml21.bottom_hole_location import BottomHoleLocation
from witsml21.data_object_reference import DataObjectReference
from witsml21.facility_lifecycle_period import FacilityLifecyclePeriod
from witsml21.facility_lifecycle_state import FacilityLifecycleState
from witsml21.facility_operator import FacilityOperator
from witsml21.license_period import LicensePeriod
from witsml21.measured_depth import MeasuredDepth
from witsml21.time_measure import TimeMeasure
from witsml21.well_fluid import WellFluid
from witsml21.well_purpose import WellPurpose
from witsml21.well_purpose_period import WellPurposePeriod
from witsml21.well_status import WellStatus
from witsml21.well_status_period import WellStatusPeriod
from witsml21.wellbore_shape import WellboreShape
from witsml21.wellbore_type import WellboreType

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class Wellbore(AbstractActiveObject):
    """Used to capture the general information about a wellbore.

    A wellbore represents the path from the parent Well’s surface
    location to a unique bottomhole location. The wellbore object is
    uniquely identified within the context of one well object.

    :ivar geographic_bottom_hole_location: The bottom hole location in
        geographic coordinates. Location MUST be a geographic position.
    :ivar number: Operator borehole number.
    :ivar projected_bottom_hole_location: The bottom hole location in
        projected coordinates. Location MUST be a projected position.
    :ivar suffix_api: API suffix.
    :ivar num_license: License number of the wellbore.
    :ivar license_history: The history of license numbers for the
        wellbore.
    :ivar num_govt: Government assigned number.
    :ivar unique_identifier: A human-readable unique identifier assigned
        to the wellbore. Commonly referred to as a UWI.
    :ivar slot_name: The well's slot name.
    :ivar operator: Pointer to a BusinessAssociate representing the
        operating company.
    :ivar original_operator: Pointer to a BusinessAssociate representing
        the original operator of the wellbore. This may be different
        than the current operator.
    :ivar operator_history: The history of operators for the wellbore
        optionally including the dates and times that they were
        operators. If provided, the first operator should be the same as
        OriginalOperator and the last operator should be the same as
        Operator.
    :ivar data_source_organization: Pointer to a BusinessAssociate
        representing the company providing the data in this wellbore
        object.
    :ivar lifecycle_state: The wellbore's lifecycle state (e.g.,
        planning, constructing, operating, closing, closed).
    :ivar lifecycle_history: The wellbore's life cycle state history.
    :ivar status_wellbore: POSC wellbore status.
    :ivar status_history: History of the wellbore's POSC well status.
    :ivar purpose_wellbore: POSC wellbore purpose.
    :ivar purpose_history: History of the wellbore's POSC well purpose.
    :ivar type_wellbore: Type of wellbore.
    :ivar shape: POSC wellbore trajectory shape.
    :ivar fluid_wellbore: POSC well fluid. The type of fluid being
        produced from or injected into a wellbore facility.
    :ivar dtim_kickoff: Date and time of wellbore kickoff.
    :ivar achieved_td: True ("true" of "1") indicates that the wellbore
        has acheieved total depth. That is, drilling has completed.
        False ("false" or "0") indicates otherwise. Not given indicates
        that it is not known whether total depth has been reached.
    :ivar md: The measured depth of the borehole. If status is plugged,
        indicates the maximum depth reached before plugging. It is
        recommended that this value be updated about every 10 minutes by
        an assigned raw data provider at a site.
    :ivar tvd: The  true vertical depth of the borehole. If status is
        plugged, indicates the maximum depth reached before plugging. It
        is recommended that this value be updated about every 10 minutes
        by an assigned raw data provider at a site.
    :ivar md_bit: The measured depth of the bit. If isActive=false then
        this value is not relevant. It is recommended that this value be
        updated about every 10 minutes by an assigned raw data provider
        at a site.
    :ivar tvd_bit: The true vertical depth of the bit. If isActive=false
        then this value is not relevant. It is recommended that this
        value be updated about every 10 minutes by an assigned raw data
        provider at a site.
    :ivar md_kickoff: Kickoff measured depth of the wellbore.
    :ivar tvd_kickoff: Kickoff true vertical depth of the wellbore.
    :ivar md_planned: Planned measured depth for the wellbore total
        depth.
    :ivar tvd_planned: Planned true vertical depth for the wellbore
        total depth.
    :ivar md_sub_sea_planned: Planned measured for the wellbore total
        depth - with respect to seabed.
    :ivar tvd_sub_sea_planned: Planned true vertical depth for the
        wellbore total depth - with respect to seabed.
    :ivar day_target: Target days for drilling wellbore.
    :ivar target_formation: A formation of interest for which the
        Wellbore is drilled to interact with.
    :ivar target_geologic_unit_interpretation: Pointer to a RESQML
        GeologicUnitInterpretation that represents a geologic unit of
        interest for which the Wellbore is drilled to interact with.
    :ivar default_md_datum:
    :ivar default_tvd_datum:
    :ivar well:
    :ivar parent_wellbore:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/witsmlv2"

    geographic_bottom_hole_location: Optional[BottomHoleLocation] = field(
        default=None,
        metadata={
            "name": "GeographicBottomHoleLocation",
            "type": "Element",
        }
    )
    number: Optional[str] = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Element",
            "max_length": 64,
        }
    )
    projected_bottom_hole_location: Optional[BottomHoleLocation] = field(
        default=None,
        metadata={
            "name": "ProjectedBottomHoleLocation",
            "type": "Element",
        }
    )
    suffix_api: Optional[str] = field(
        default=None,
        metadata={
            "name": "SuffixAPI",
            "type": "Element",
            "max_length": 64,
        }
    )
    num_license: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumLicense",
            "type": "Element",
            "max_length": 64,
        }
    )
    license_history: List[LicensePeriod] = field(
        default_factory=list,
        metadata={
            "name": "LicenseHistory",
            "type": "Element",
        }
    )
    num_govt: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumGovt",
            "type": "Element",
            "max_length": 64,
        }
    )
    unique_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "UniqueIdentifier",
            "type": "Element",
            "max_length": 64,
        }
    )
    slot_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SlotName",
            "type": "Element",
            "max_length": 64,
        }
    )
    operator: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Operator",
            "type": "Element",
        }
    )
    original_operator: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "OriginalOperator",
            "type": "Element",
        }
    )
    operator_history: List[FacilityOperator] = field(
        default_factory=list,
        metadata={
            "name": "OperatorHistory",
            "type": "Element",
        }
    )
    data_source_organization: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "DataSourceOrganization",
            "type": "Element",
        }
    )
    lifecycle_state: Optional[Union[FacilityLifecycleState, str]] = field(
        default=None,
        metadata={
            "name": "LifecycleState",
            "type": "Element",
            "pattern": r".*:.*",
        }
    )
    lifecycle_history: List[FacilityLifecyclePeriod] = field(
        default_factory=list,
        metadata={
            "name": "LifecycleHistory",
            "type": "Element",
        }
    )
    status_wellbore: Optional[WellStatus] = field(
        default=None,
        metadata={
            "name": "StatusWellbore",
            "type": "Element",
        }
    )
    status_history: List[WellStatusPeriod] = field(
        default_factory=list,
        metadata={
            "name": "StatusHistory",
            "type": "Element",
        }
    )
    purpose_wellbore: Optional[WellPurpose] = field(
        default=None,
        metadata={
            "name": "PurposeWellbore",
            "type": "Element",
        }
    )
    purpose_history: List[WellPurposePeriod] = field(
        default_factory=list,
        metadata={
            "name": "PurposeHistory",
            "type": "Element",
        }
    )
    type_wellbore: Optional[WellboreType] = field(
        default=None,
        metadata={
            "name": "TypeWellbore",
            "type": "Element",
        }
    )
    shape: Optional[WellboreShape] = field(
        default=None,
        metadata={
            "name": "Shape",
            "type": "Element",
        }
    )
    fluid_wellbore: Optional[WellFluid] = field(
        default=None,
        metadata={
            "name": "FluidWellbore",
            "type": "Element",
        }
    )
    dtim_kickoff: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimKickoff",
            "type": "Element",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    achieved_td: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AchievedTD",
            "type": "Element",
        }
    )
    md: Optional[MeasuredDepth] = field(
        default=None,
        metadata={
            "name": "Md",
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
    md_bit: Optional[MeasuredDepth] = field(
        default=None,
        metadata={
            "name": "MdBit",
            "type": "Element",
        }
    )
    tvd_bit: Optional[AbstractVerticalDepth] = field(
        default=None,
        metadata={
            "name": "TvdBit",
            "type": "Element",
        }
    )
    md_kickoff: Optional[MeasuredDepth] = field(
        default=None,
        metadata={
            "name": "MdKickoff",
            "type": "Element",
        }
    )
    tvd_kickoff: Optional[AbstractVerticalDepth] = field(
        default=None,
        metadata={
            "name": "TvdKickoff",
            "type": "Element",
        }
    )
    md_planned: Optional[MeasuredDepth] = field(
        default=None,
        metadata={
            "name": "MdPlanned",
            "type": "Element",
        }
    )
    tvd_planned: Optional[AbstractVerticalDepth] = field(
        default=None,
        metadata={
            "name": "TvdPlanned",
            "type": "Element",
        }
    )
    md_sub_sea_planned: Optional[MeasuredDepth] = field(
        default=None,
        metadata={
            "name": "MdSubSeaPlanned",
            "type": "Element",
        }
    )
    tvd_sub_sea_planned: Optional[AbstractVerticalDepth] = field(
        default=None,
        metadata={
            "name": "TvdSubSeaPlanned",
            "type": "Element",
        }
    )
    day_target: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "DayTarget",
            "type": "Element",
        }
    )
    target_formation: List[str] = field(
        default_factory=list,
        metadata={
            "name": "TargetFormation",
            "type": "Element",
            "max_length": 64,
        }
    )
    target_geologic_unit_interpretation: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "TargetGeologicUnitInterpretation",
            "type": "Element",
        }
    )
    default_md_datum: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "DefaultMdDatum",
            "type": "Element",
        }
    )
    default_tvd_datum: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "DefaultTvdDatum",
            "type": "Element",
        }
    )
    well: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Well",
            "type": "Element",
            "required": True,
        }
    )
    parent_wellbore: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "ParentWellbore",
            "type": "Element",
        }
    )
