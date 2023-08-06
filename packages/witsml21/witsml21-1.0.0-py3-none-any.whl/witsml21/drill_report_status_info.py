from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.abstract_elevation import AbstractElevation
from witsml21.abstract_vertical_depth import AbstractVerticalDepth
from witsml21.cost import Cost
from witsml21.data_object_reference import DataObjectReference
from witsml21.extension_name_value import ExtensionNameValue
from witsml21.length_measure import LengthMeasure
from witsml21.length_per_time_measure import LengthPerTimeMeasure
from witsml21.mass_per_volume_measure import MassPerVolumeMeasure
from witsml21.measured_depth import MeasuredDepth
from witsml21.pres_test_type import PresTestType
from witsml21.pressure_measure import PressureMeasure
from witsml21.time_measure import TimeMeasure
from witsml21.volume_measure import VolumeMeasure
from witsml21.wellbore_type import WellboreType

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class DrillReportStatusInfo:
    """
    General status information for the drill report period.

    :ivar dtim: The date and time for which the well status is reported.
    :ivar md: Wellbore measured depth at the end of the report period.
    :ivar tvd: Wellbore true vertical depth at the end of the report.
    :ivar md_plug_top: The measured plug back depth.
    :ivar dia_hole: Hole nominal inside diameter.
    :ivar md_dia_hole_start: Measured depth to the start of the current
        hole diameter.
    :ivar dia_pilot: Pilot hole nominal inside diameter.
    :ivar md_dia_pilot_plan: The planned measured depth of the pilot
        hole.
    :ivar tvd_dia_pilot_plan: The planned true vertical depth of the
        pilot hole.
    :ivar type_wellbore: Type of wellbore.
    :ivar md_kickoff: Measured depth to the kickoff point of the
        wellbore.
    :ivar tvd_kickoff: True vertical depth to the kickoff point of the
        wellbore.
    :ivar strength_form: The measured formation strength. This should be
        the final measurement before the end of the report period.
    :ivar md_strength_form: The measured depth of the formation strength
        measurement.
    :ivar tvd_strength_form: The true vertical depth of the formation
        strength measurement.
    :ivar dia_csg_last: Diameter of the last casing joint.
    :ivar md_csg_last: Measured depth of the last casing joint.
    :ivar tvd_csg_last: True vertical depth of last casing joint.
    :ivar pres_test_type: The type of pressure test that was run.
    :ivar md_planned: The measured depth planned to be reached.
    :ivar dist_drill: Distance drilled.  This should be measured along
        the centerline of the wellbore.
    :ivar sum24_hr: A summary of the activities performed and the status
        of the ongoing activities.
    :ivar forecast24_hr: A summary of  planned activities for the next
        reporting period.
    :ivar rop_current: Rate of penetration at the end of the reporting
        period.
    :ivar rig_utilization: A pointer to the rig used.
    :ivar etim_start: Time from the start of operations (commonly in
        days).
    :ivar etim_spud: Time since the bit broke ground (commonly in days).
    :ivar etim_loc: Time the rig has been on location (commonly in
        days).
    :ivar etim_drill: Drilling time.
    :ivar rop_av: Average rate of penetration.
    :ivar supervisor: Name of the operator's rig supervisor.
    :ivar engineer: Name of the operator's drilling engineer.
    :ivar geologist: Name of operator's wellsite geologist.
    :ivar etim_drill_rot: Time spent rotary drilling.
    :ivar etim_drill_slid: Time spent slide drilling from the start of
        the bit run.
    :ivar etim_circ: Time spent circulating from the start of the bit
        run.
    :ivar etim_ream: Time spent reaming from the start of the bit run.
    :ivar etim_hold: Time spent with no directional drilling work
        (commonly in hours).
    :ivar etim_steering: Time spent steering the bottomhole assembly
        (commonly in hours).
    :ivar dist_drill_rot: Distance drilled: rotating.
    :ivar dist_drill_slid: Distance drilled: sliding.
    :ivar dist_ream: Distance reamed.
    :ivar dist_hold: Distance covered while holding angle with a
        steerable drilling assembly.
    :ivar dist_steering: Distance covered while actively steering with a
        steerable drilling assembly.
    :ivar num_pob: Total number of personnel on board the rig.
    :ivar num_contract: Number of contractor personnel on the rig.
    :ivar num_operator: Number of operator personnel on the rig.
    :ivar num_service: Number of service company personnel on the rig.
    :ivar num_afe: Authorization for expenditure (AFE) number that this
        cost item applies to.
    :ivar condition_hole: Description of the hole condition.
    :ivar tvd_lot: True vertical depth of a leak off test point.
    :ivar pres_lot_emw: Leak off test equivalent mud weight.
    :ivar pres_kick_tol: Kick tolerance pressure.
    :ivar vol_kick_tol: Kick tolerance volume.
    :ivar maasp: Maximum allowable shut-in casing pressure.
    :ivar tubular: A pointer to the tubular (assembly) used in this
        report period.
    :ivar parent_wellbore: References to the parent wellbore(s). These
        are the wellbore(s) from which the current wellbore (indirectly)
        kickedoff.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar elev_kelly:
    :ivar cost_day:
    :ivar cost_day_mud:
    :ivar uid: Unique identifier for this instance of
        DrillReportStatusInfo.
    """
    dtim: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTim",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    md: Optional[MeasuredDepth] = field(
        default=None,
        metadata={
            "name": "Md",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    tvd: Optional[AbstractVerticalDepth] = field(
        default=None,
        metadata={
            "name": "Tvd",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    md_plug_top: Optional[MeasuredDepth] = field(
        default=None,
        metadata={
            "name": "MdPlugTop",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    dia_hole: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "DiaHole",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    md_dia_hole_start: Optional[MeasuredDepth] = field(
        default=None,
        metadata={
            "name": "MdDiaHoleStart",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    dia_pilot: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "DiaPilot",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    md_dia_pilot_plan: Optional[MeasuredDepth] = field(
        default=None,
        metadata={
            "name": "MdDiaPilotPlan",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    tvd_dia_pilot_plan: Optional[AbstractVerticalDepth] = field(
        default=None,
        metadata={
            "name": "TvdDiaPilotPlan",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    type_wellbore: Optional[WellboreType] = field(
        default=None,
        metadata={
            "name": "TypeWellbore",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    md_kickoff: Optional[MeasuredDepth] = field(
        default=None,
        metadata={
            "name": "MdKickoff",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    tvd_kickoff: Optional[MeasuredDepth] = field(
        default=None,
        metadata={
            "name": "TvdKickoff",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    strength_form: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "StrengthForm",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    md_strength_form: Optional[MeasuredDepth] = field(
        default=None,
        metadata={
            "name": "MdStrengthForm",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    tvd_strength_form: Optional[AbstractVerticalDepth] = field(
        default=None,
        metadata={
            "name": "TvdStrengthForm",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    dia_csg_last: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "DiaCsgLast",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    md_csg_last: Optional[MeasuredDepth] = field(
        default=None,
        metadata={
            "name": "MdCsgLast",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    tvd_csg_last: Optional[AbstractVerticalDepth] = field(
        default=None,
        metadata={
            "name": "TvdCsgLast",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pres_test_type: Optional[PresTestType] = field(
        default=None,
        metadata={
            "name": "PresTestType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    md_planned: Optional[MeasuredDepth] = field(
        default=None,
        metadata={
            "name": "MdPlanned",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    dist_drill: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "DistDrill",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    sum24_hr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Sum24Hr",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 2000,
        }
    )
    forecast24_hr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Forecast24Hr",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 2000,
        }
    )
    rop_current: Optional[LengthPerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "RopCurrent",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    rig_utilization: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "RigUtilization",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    etim_start: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "ETimStart",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    etim_spud: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "ETimSpud",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    etim_loc: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "ETimLoc",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    etim_drill: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "ETimDrill",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    rop_av: Optional[LengthPerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "RopAv",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    supervisor: Optional[str] = field(
        default=None,
        metadata={
            "name": "Supervisor",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    engineer: Optional[str] = field(
        default=None,
        metadata={
            "name": "Engineer",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    geologist: Optional[str] = field(
        default=None,
        metadata={
            "name": "Geologist",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    etim_drill_rot: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "ETimDrillRot",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    etim_drill_slid: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "ETimDrillSlid",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    etim_circ: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "ETimCirc",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    etim_ream: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "ETimReam",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    etim_hold: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "ETimHold",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    etim_steering: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "ETimSteering",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    dist_drill_rot: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "DistDrillRot",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    dist_drill_slid: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "DistDrillSlid",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    dist_ream: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "DistReam",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    dist_hold: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "DistHold",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    dist_steering: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "DistSteering",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    num_pob: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumPob",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    num_contract: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumContract",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    num_operator: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumOperator",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    num_service: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumService",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    num_afe: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumAFE",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    condition_hole: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConditionHole",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    tvd_lot: Optional[AbstractVerticalDepth] = field(
        default=None,
        metadata={
            "name": "TvdLot",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pres_lot_emw: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "PresLotEmw",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pres_kick_tol: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "PresKickTol",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    vol_kick_tol: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "VolKickTol",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    maasp: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "Maasp",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    tubular: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Tubular",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    parent_wellbore: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "ParentWellbore",
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
    elev_kelly: Optional[AbstractElevation] = field(
        default=None,
        metadata={
            "name": "ElevKelly",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    cost_day: Optional[Cost] = field(
        default=None,
        metadata={
            "name": "CostDay",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    cost_day_mud: Optional[Cost] = field(
        default=None,
        metadata={
            "name": "CostDayMud",
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
