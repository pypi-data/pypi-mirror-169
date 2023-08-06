from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.abstract_object import AbstractObject
from witsml21.abstract_vertical_depth import AbstractVerticalDepth
from witsml21.cost import Cost
from witsml21.data_object_reference import DataObjectReference
from witsml21.day_cost import DayCost
from witsml21.drill_activity import DrillActivity
from witsml21.drilling_params import DrillingParams
from witsml21.fluid import Fluid
from witsml21.hse import Hse
from witsml21.inventory import Inventory
from witsml21.length_measure import LengthMeasure
from witsml21.length_per_time_measure import LengthPerTimeMeasure
from witsml21.mass_per_volume_measure import MassPerVolumeMeasure
from witsml21.measured_depth import MeasuredDepth
from witsml21.mud_volume import MudVolume
from witsml21.personnel import Personnel
from witsml21.pit_volume import PitVolume
from witsml21.pressure_measure import PressureMeasure
from witsml21.pump_op import PumpOp
from witsml21.rig_response import RigResponse
from witsml21.scr import Scr
from witsml21.shaker_op import ShakerOp
from witsml21.support_craft import SupportCraft
from witsml21.time_measure import TimeMeasure
from witsml21.trajectory_report import TrajectoryReport
from witsml21.volume_measure import VolumeMeasure
from witsml21.weather import Weather
from witsml21.wellbore_geometry_report import WellboreGeometryReport

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class OpsReport(AbstractObject):
    """Used to capture a daily drilling report focused on reporting from the
    service company to the operator.

    For a similar object whose focus is operator to partner or to
    governmental agency, see DrillReport. This object is uniquely
    identified within the context of one wellbore object.

    :ivar condition_hole: Hole condition description.
    :ivar cost_day: Daily cost.
    :ivar cost_day_mud: Daily mud cost.
    :ivar dia_csg_last: Diameter of the last casing installed.
    :ivar dia_hole: Hole diameter.
    :ivar dist_drill: Distance drilled since the previous report.
    :ivar dist_drill_rot: Distance drilled: rotating.
    :ivar dist_drill_slid: Distance drilled: sliding.
    :ivar dist_hold: Distance covered while holding angle with a
        steerable drilling assembly.
    :ivar dist_ream: Distance reamed.
    :ivar dist_steering: Distance covered while actively steering with a
        steerable drilling assembly.
    :ivar dtim: Date and time the information is related to.
    :ivar engineer: Name of the engineer.
    :ivar etim_circ: Time spent circulating from start of the bit run.
    :ivar etim_drill: Drilling time.
    :ivar etim_drill_rot: Time spent rotary drilling for the report
        interval.
    :ivar etim_drill_slid: Time spent slide drilling from start of the
        bit run.
    :ivar etim_hold: Time spent with no directional drilling work
        (commonly in hours).
    :ivar etim_loc: Time the rig has been on location (commonly in
        days).
    :ivar etim_ream: Time spent reaming from start of the bit run.
    :ivar etim_spud: Time since the bit broke ground (commonly in days).
    :ivar etim_start: Time from the start of operations (commonly in
        days).
    :ivar etim_steering: Time spent steering the bottomhole assembly
        (commonly in hours).
    :ivar forecast24_hr: Forecast of activities for the next 24 hrs.
    :ivar geologist: Name of the operator's wellsite geologist.
    :ivar lithology: Description of the lithology for the interval.
    :ivar maasp: Maximum allowable shut-in casing pressure.
    :ivar md_csg_last: Measured depth of last casing.
    :ivar md_planned: Measured depth of plan for this day number.
    :ivar md_report: The measured depth of the wellbore.
    :ivar name_formation: Name of the formation.
    :ivar num_afe: Authorization for expenditure (AFE) number that this
        cost item applies to.
    :ivar num_contract: Number of contractor personnel on board the rig.
    :ivar num_operator: Number of operator personnel on board the rig.
    :ivar num_pob: Total number of personnel on board the rig.
    :ivar num_service: Number of service company personnel on board the
        rig.
    :ivar pres_kick_tol: Kick tolerance pressure.
    :ivar pres_lot_emw: Leak off test equivalent mud weight.
    :ivar rig_utilization: A pointer to the rig used in this reporting
        period.
    :ivar rop_av: Average rate of penetration through the interval.
    :ivar rop_current: Rate of penetration at report time.
    :ivar status_current: Current status description.
    :ivar sum24_hr: Summary of the operations and events for the
        reporting period (the previous 24 hours).
    :ivar supervisor: Name of the operator's rig supervisor.
    :ivar tubular: A pointer to the tubular assembly (as specified in
        the Tubular object) used in this report period.
    :ivar tvd_csg_last: True vertical depth of the last casing
        installed.
    :ivar tvd_lot: True vertical depth of the leak-off test point.
    :ivar tvd_report: True vertical depth of the wellbore.
    :ivar vol_kick_tol: Kick tolerance volume.
    :ivar activity:
    :ivar drilling_params:
    :ivar wb_geometry:
    :ivar day_cost:
    :ivar trajectory_stations:
    :ivar fluid:
    :ivar scr:
    :ivar rig_response:
    :ivar shaker_op:
    :ivar hse:
    :ivar support_craft:
    :ivar weather:
    :ivar wellbore:
    :ivar mud_volume:
    :ivar bulk_inventory:
    :ivar mud_inventory:
    :ivar personnel:
    :ivar pump_op:
    :ivar pit_volume:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/witsmlv2"

    condition_hole: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConditionHole",
            "type": "Element",
            "max_length": 64,
        }
    )
    cost_day: Optional[Cost] = field(
        default=None,
        metadata={
            "name": "CostDay",
            "type": "Element",
        }
    )
    cost_day_mud: Optional[Cost] = field(
        default=None,
        metadata={
            "name": "CostDayMud",
            "type": "Element",
        }
    )
    dia_csg_last: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "DiaCsgLast",
            "type": "Element",
        }
    )
    dia_hole: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "DiaHole",
            "type": "Element",
        }
    )
    dist_drill: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "DistDrill",
            "type": "Element",
        }
    )
    dist_drill_rot: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "DistDrillRot",
            "type": "Element",
        }
    )
    dist_drill_slid: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "DistDrillSlid",
            "type": "Element",
        }
    )
    dist_hold: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "DistHold",
            "type": "Element",
        }
    )
    dist_ream: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "DistReam",
            "type": "Element",
        }
    )
    dist_steering: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "DistSteering",
            "type": "Element",
        }
    )
    dtim: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTim",
            "type": "Element",
            "required": True,
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    engineer: Optional[str] = field(
        default=None,
        metadata={
            "name": "Engineer",
            "type": "Element",
            "max_length": 64,
        }
    )
    etim_circ: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "ETimCirc",
            "type": "Element",
        }
    )
    etim_drill: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "ETimDrill",
            "type": "Element",
        }
    )
    etim_drill_rot: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "ETimDrillRot",
            "type": "Element",
        }
    )
    etim_drill_slid: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "ETimDrillSlid",
            "type": "Element",
        }
    )
    etim_hold: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "ETimHold",
            "type": "Element",
        }
    )
    etim_loc: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "ETimLoc",
            "type": "Element",
        }
    )
    etim_ream: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "ETimReam",
            "type": "Element",
        }
    )
    etim_spud: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "ETimSpud",
            "type": "Element",
        }
    )
    etim_start: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "ETimStart",
            "type": "Element",
        }
    )
    etim_steering: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "ETimSteering",
            "type": "Element",
        }
    )
    forecast24_hr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Forecast24Hr",
            "type": "Element",
            "max_length": 2000,
        }
    )
    geologist: Optional[str] = field(
        default=None,
        metadata={
            "name": "Geologist",
            "type": "Element",
            "max_length": 64,
        }
    )
    lithology: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lithology",
            "type": "Element",
            "max_length": 64,
        }
    )
    maasp: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "Maasp",
            "type": "Element",
        }
    )
    md_csg_last: Optional[MeasuredDepth] = field(
        default=None,
        metadata={
            "name": "MdCsgLast",
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
    md_report: Optional[MeasuredDepth] = field(
        default=None,
        metadata={
            "name": "MdReport",
            "type": "Element",
        }
    )
    name_formation: Optional[str] = field(
        default=None,
        metadata={
            "name": "NameFormation",
            "type": "Element",
            "max_length": 64,
        }
    )
    num_afe: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumAFE",
            "type": "Element",
            "max_length": 64,
        }
    )
    num_contract: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumContract",
            "type": "Element",
        }
    )
    num_operator: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumOperator",
            "type": "Element",
        }
    )
    num_pob: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumPob",
            "type": "Element",
        }
    )
    num_service: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumService",
            "type": "Element",
        }
    )
    pres_kick_tol: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "PresKickTol",
            "type": "Element",
        }
    )
    pres_lot_emw: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "PresLotEmw",
            "type": "Element",
        }
    )
    rig_utilization: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "RigUtilization",
            "type": "Element",
        }
    )
    rop_av: Optional[LengthPerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "RopAv",
            "type": "Element",
        }
    )
    rop_current: Optional[LengthPerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "RopCurrent",
            "type": "Element",
        }
    )
    status_current: Optional[str] = field(
        default=None,
        metadata={
            "name": "StatusCurrent",
            "type": "Element",
            "max_length": 2000,
        }
    )
    sum24_hr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Sum24Hr",
            "type": "Element",
            "max_length": 2000,
        }
    )
    supervisor: Optional[str] = field(
        default=None,
        metadata={
            "name": "Supervisor",
            "type": "Element",
            "max_length": 64,
        }
    )
    tubular: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Tubular",
            "type": "Element",
        }
    )
    tvd_csg_last: Optional[AbstractVerticalDepth] = field(
        default=None,
        metadata={
            "name": "TvdCsgLast",
            "type": "Element",
        }
    )
    tvd_lot: Optional[AbstractVerticalDepth] = field(
        default=None,
        metadata={
            "name": "TvdLot",
            "type": "Element",
        }
    )
    tvd_report: Optional[AbstractVerticalDepth] = field(
        default=None,
        metadata={
            "name": "TvdReport",
            "type": "Element",
        }
    )
    vol_kick_tol: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "VolKickTol",
            "type": "Element",
        }
    )
    activity: List[DrillActivity] = field(
        default_factory=list,
        metadata={
            "name": "Activity",
            "type": "Element",
        }
    )
    drilling_params: List[DrillingParams] = field(
        default_factory=list,
        metadata={
            "name": "DrillingParams",
            "type": "Element",
        }
    )
    wb_geometry: Optional[WellboreGeometryReport] = field(
        default=None,
        metadata={
            "name": "WbGeometry",
            "type": "Element",
        }
    )
    day_cost: List[DayCost] = field(
        default_factory=list,
        metadata={
            "name": "DayCost",
            "type": "Element",
        }
    )
    trajectory_stations: Optional[TrajectoryReport] = field(
        default=None,
        metadata={
            "name": "TrajectoryStations",
            "type": "Element",
        }
    )
    fluid: List[Fluid] = field(
        default_factory=list,
        metadata={
            "name": "Fluid",
            "type": "Element",
        }
    )
    scr: List[Scr] = field(
        default_factory=list,
        metadata={
            "name": "Scr",
            "type": "Element",
        }
    )
    rig_response: Optional[RigResponse] = field(
        default=None,
        metadata={
            "name": "RigResponse",
            "type": "Element",
        }
    )
    shaker_op: List[ShakerOp] = field(
        default_factory=list,
        metadata={
            "name": "ShakerOp",
            "type": "Element",
        }
    )
    hse: Optional[Hse] = field(
        default=None,
        metadata={
            "name": "Hse",
            "type": "Element",
        }
    )
    support_craft: List[SupportCraft] = field(
        default_factory=list,
        metadata={
            "name": "SupportCraft",
            "type": "Element",
        }
    )
    weather: List[Weather] = field(
        default_factory=list,
        metadata={
            "name": "Weather",
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
    mud_volume: Optional[MudVolume] = field(
        default=None,
        metadata={
            "name": "MudVolume",
            "type": "Element",
        }
    )
    bulk_inventory: List[Inventory] = field(
        default_factory=list,
        metadata={
            "name": "BulkInventory",
            "type": "Element",
        }
    )
    mud_inventory: List[Inventory] = field(
        default_factory=list,
        metadata={
            "name": "MudInventory",
            "type": "Element",
        }
    )
    personnel: List[Personnel] = field(
        default_factory=list,
        metadata={
            "name": "Personnel",
            "type": "Element",
        }
    )
    pump_op: List[PumpOp] = field(
        default_factory=list,
        metadata={
            "name": "PumpOp",
            "type": "Element",
        }
    )
    pit_volume: List[PitVolume] = field(
        default_factory=list,
        metadata={
            "name": "PitVolume",
            "type": "Element",
        }
    )
