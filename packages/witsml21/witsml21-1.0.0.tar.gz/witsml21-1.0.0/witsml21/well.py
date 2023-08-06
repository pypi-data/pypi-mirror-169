from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional, Union
from witsml21.abstract_active_object import AbstractActiveObject
from witsml21.abstract_elevation import AbstractElevation
from witsml21.abstract_position import AbstractPosition
from witsml21.data_object_reference import DataObjectReference
from witsml21.dimensionless_measure import DimensionlessMeasure
from witsml21.facility_lifecycle_period import FacilityLifecyclePeriod
from witsml21.facility_lifecycle_state import FacilityLifecycleState
from witsml21.facility_operator import FacilityOperator
from witsml21.geographic2d_position import Geographic2DPosition
from witsml21.length_measure import LengthMeasure
from witsml21.license_period import LicensePeriod
from witsml21.operating_environment import OperatingEnvironment
from witsml21.projected2d_position import Projected2DPosition
from witsml21.well_direction import WellDirection
from witsml21.well_fluid import WellFluid
from witsml21.well_interest import WellInterest
from witsml21.well_purpose import WellPurpose
from witsml21.well_purpose_period import WellPurposePeriod
from witsml21.well_status import WellStatus
from witsml21.well_status_period import WellStatusPeriod

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class Well(AbstractActiveObject):
    """Used to capture the general information about a well.

    Sometimes  called a "well header". Contains all information that is
    the same for all wellbores (sidetracks).

    :ivar unique_identifier: A human-readable unique identifier assigned
        to the well. Commonly referred to as a UWI.
    :ivar name_legal: Legal name of the well.
    :ivar num_govt: Government assigned well number.
    :ivar num_api: American Petroleum Institute well number.
    :ivar operating_environment: Environment in which the well operates
        (e.eg, onshore, offshore, etc.).
    :ivar time_zone: The time zone in which the well is located. It is
        the deviation in hours and minutes from UTC. This should be the
        normal time zone at the well and not a seasonally-adjusted
        value, such as daylight savings time.
    :ivar basin: Basin in which the well is located.
    :ivar play: Play in which the well is located.
    :ivar prospect: Prospect in which the well is located.
    :ivar field_value: Name of the field in which the well is located.
    :ivar country: Country in which the well is located.
    :ivar state: State or province in which the well is located.
    :ivar county: County in which the well is located.
    :ivar region: Geo-political region in which the well is located.
    :ivar district: Geo-political district name.
    :ivar num_license: License number of the well.
    :ivar dtim_license: Date and time the license  was issued.
    :ivar license_history: The history of license numbers for the well.
    :ivar block: Block name in which the well is located.
    :ivar interest_type: Reasons for interest in the well or information
        about the well.
    :ivar pc_interest: Interest for operator. Commonly in percent.
    :ivar slot_name: The well's slot name.
    :ivar life_cycle_state: The well's life cycle state (e.g., planning,
        constructing, operating, closing, closed).
    :ivar life_cycle_history: The well's life cycle state history.
    :ivar operator: Pointer to a BusinessAssociate representing the
        operating company.
    :ivar operator_div: Division of the operator company.
    :ivar original_operator: Pointer to a BusinessAssociate representing
        the original operator of the well. This may be different than
        the current operator.
    :ivar operator_history: The history of operators for the well
        optionally including the dates and times that they were
        operators. If provided, the first operator should be the same as
        OriginalOperator and the last operator should be the same as
        Operator.
    :ivar status_well: POSC well status.
    :ivar status_history: History of the well's POSC well status.
    :ivar purpose_well: POSC well purpose.
    :ivar purpose_history: History of the well's POSC well purpose.
    :ivar fluid_well: POSC well fluid. The type of fluid being produced
        from or injected into a well facility.
    :ivar direction_well: POSC well direction. The direction of the flow
        of the fluids in a well facility (generally, injected or
        produced, or some combination).
    :ivar dtim_spud: Date and time at which the well was spudded.
    :ivar dtim_pa: Date and time at which the well was plugged and
        abandoned.
    :ivar water_depth: Depth of water (not land rigs).
    :ivar informational_geographic_location_wgs84: The approximate 2D
        well location. Intended for use cases where a low-fidelity,
        approximate location are acceptable such as displaying the well
        on a map in a dashboard.
    :ivar informational_projected_location:
    :ivar data_source_organization: Pointer to a BusinessAssociate
        representing the company providing the data in this well object.
    :ivar wellhead_elevation:
    :ivar ground_elevation:
    :ivar well_surface_location: The surface location of the well. This
        is shared by all wellbores within the well.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/witsmlv2"

    unique_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "UniqueIdentifier",
            "type": "Element",
            "max_length": 64,
        }
    )
    name_legal: Optional[str] = field(
        default=None,
        metadata={
            "name": "NameLegal",
            "type": "Element",
            "max_length": 64,
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
    num_api: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumAPI",
            "type": "Element",
            "max_length": 64,
        }
    )
    operating_environment: Optional[Union[OperatingEnvironment, str]] = field(
        default=None,
        metadata={
            "name": "OperatingEnvironment",
            "type": "Element",
            "pattern": r".*:.*",
        }
    )
    time_zone: Optional[str] = field(
        default=None,
        metadata={
            "name": "TimeZone",
            "type": "Element",
            "max_length": 64,
            "pattern": r"[Z]|([\-+](([01][0-9])|(2[0-3])):[0-5][0-9])",
        }
    )
    basin: Optional[str] = field(
        default=None,
        metadata={
            "name": "Basin",
            "type": "Element",
            "max_length": 64,
        }
    )
    play: Optional[str] = field(
        default=None,
        metadata={
            "name": "Play",
            "type": "Element",
            "max_length": 64,
        }
    )
    prospect: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prospect",
            "type": "Element",
            "max_length": 64,
        }
    )
    field_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Field",
            "type": "Element",
            "max_length": 64,
        }
    )
    country: Optional[str] = field(
        default=None,
        metadata={
            "name": "Country",
            "type": "Element",
            "max_length": 64,
        }
    )
    state: Optional[str] = field(
        default=None,
        metadata={
            "name": "State",
            "type": "Element",
            "max_length": 64,
        }
    )
    county: Optional[str] = field(
        default=None,
        metadata={
            "name": "County",
            "type": "Element",
            "max_length": 64,
        }
    )
    region: Optional[str] = field(
        default=None,
        metadata={
            "name": "Region",
            "type": "Element",
            "max_length": 64,
        }
    )
    district: Optional[str] = field(
        default=None,
        metadata={
            "name": "District",
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
    dtim_license: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimLicense",
            "type": "Element",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    license_history: List[LicensePeriod] = field(
        default_factory=list,
        metadata={
            "name": "LicenseHistory",
            "type": "Element",
        }
    )
    block: Optional[str] = field(
        default=None,
        metadata={
            "name": "Block",
            "type": "Element",
            "max_length": 64,
        }
    )
    interest_type: Optional[Union[WellInterest, str]] = field(
        default=None,
        metadata={
            "name": "InterestType",
            "type": "Element",
            "pattern": r".*:.*",
        }
    )
    pc_interest: Optional[DimensionlessMeasure] = field(
        default=None,
        metadata={
            "name": "PcInterest",
            "type": "Element",
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
    life_cycle_state: Optional[Union[FacilityLifecycleState, str]] = field(
        default=None,
        metadata={
            "name": "LifeCycleState",
            "type": "Element",
            "pattern": r".*:.*",
        }
    )
    life_cycle_history: List[FacilityLifecyclePeriod] = field(
        default_factory=list,
        metadata={
            "name": "LifeCycleHistory",
            "type": "Element",
        }
    )
    operator: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Operator",
            "type": "Element",
        }
    )
    operator_div: Optional[str] = field(
        default=None,
        metadata={
            "name": "OperatorDiv",
            "type": "Element",
            "max_length": 64,
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
    status_well: Optional[WellStatus] = field(
        default=None,
        metadata={
            "name": "StatusWell",
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
    purpose_well: Optional[WellPurpose] = field(
        default=None,
        metadata={
            "name": "PurposeWell",
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
    fluid_well: Optional[WellFluid] = field(
        default=None,
        metadata={
            "name": "FluidWell",
            "type": "Element",
        }
    )
    direction_well: Optional[WellDirection] = field(
        default=None,
        metadata={
            "name": "DirectionWell",
            "type": "Element",
        }
    )
    dtim_spud: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimSpud",
            "type": "Element",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    dtim_pa: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimPa",
            "type": "Element",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    water_depth: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "WaterDepth",
            "type": "Element",
        }
    )
    informational_geographic_location_wgs84: Optional[Geographic2DPosition] = field(
        default=None,
        metadata={
            "name": "InformationalGeographicLocationWGS84",
            "type": "Element",
        }
    )
    informational_projected_location: Optional[Projected2DPosition] = field(
        default=None,
        metadata={
            "name": "InformationalProjectedLocation",
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
    wellhead_elevation: Optional[AbstractElevation] = field(
        default=None,
        metadata={
            "name": "WellheadElevation",
            "type": "Element",
        }
    )
    ground_elevation: Optional[AbstractElevation] = field(
        default=None,
        metadata={
            "name": "GroundElevation",
            "type": "Element",
        }
    )
    well_surface_location: List[AbstractPosition] = field(
        default_factory=list,
        metadata={
            "name": "WellSurfaceLocation",
            "type": "Element",
        }
    )
