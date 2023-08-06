from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.angular_velocity_measure import AngularVelocityMeasure
from witsml21.data_object_reference import DataObjectReference
from witsml21.extension_name_value import ExtensionNameValue
from witsml21.force_measure import ForceMeasure
from witsml21.length_measure import LengthMeasure
from witsml21.length_per_time_measure import LengthPerTimeMeasure
from witsml21.mass_per_volume_measure import MassPerVolumeMeasure
from witsml21.measured_depth import MeasuredDepth
from witsml21.moment_of_force_measure import MomentOfForceMeasure
from witsml21.mud_class import MudType
from witsml21.mud_sub_class import MudSubType
from witsml21.plane_angle_measure import PlaneAngleMeasure
from witsml21.power_measure import PowerMeasure
from witsml21.pressure_measure import PressureMeasure
from witsml21.thermodynamic_temperature_measure import ThermodynamicTemperatureMeasure
from witsml21.time_measure import TimeMeasure
from witsml21.volume_per_time_measure import VolumePerTimeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class DrillingParams:
    """
    The bottomhole assembly drilling parameters schema, which contains
    statistical and calculated operations data for the run, related to depths,
    activities, temperature, pressure, flow rates, torque, etc.

    :ivar etim_op_bit: Operating time spent by bit for run. BUSINESS
        RULE: When reporting an actual as opposed to design, this is
        required.
    :ivar md_hole_start: Measured depth at start of the run.
    :ivar md_hole_stop: Measured depth at the end of the run.
    :ivar hkld_rot: Hookload: rotating.
    :ivar over_pull: Overpull = HkldUp - HkldRot
    :ivar slack_off: Slackoff = HkldRot  - HkdDown.
    :ivar hkld_up: Hookload when the string is moving up.
    :ivar hkld_dn: Hookload when the string is moving down.
    :ivar tq_on_bot_av: Average Torque: on bottom.
    :ivar tq_on_bot_mx: Maximum torque: on bottom.
    :ivar tq_on_bot_mn: Minimum torque: on bottom.
    :ivar tq_off_bot_av: Average torque: off bottom.
    :ivar tq_dh_av: Average torque: downhole.
    :ivar wt_above_jar: Weight of the string above the jars.
    :ivar wt_below_jar: Weight  of the string below the jars.
    :ivar wt_mud: Drilling fluid density.
    :ivar flowrate_pump_av: Average mud pump flow rate.
    :ivar flowrate_pump_mx: Maximum mud pump flow rate.
    :ivar flowrate_pump_mn: Minimum mud pump flow rate.
    :ivar vel_nozzle_av: Bit nozzle average velocity.
    :ivar pow_bit: Bit hydraulic.
    :ivar pres_drop_bit: Pressure drop in bit.
    :ivar ctim_hold: Time spent on hold from start of bit run.
    :ivar ctim_steering: Time spent steering from start of bit run.
    :ivar ctim_drill_rot: Time spent rotary drilling from start of bit
        run.
    :ivar ctim_drill_slid: Time spent slide drilling from start of bit
        run.
    :ivar ctim_circ: Time spent circulating from start of bit run.
    :ivar ctim_ream: Time spent reaming from start of bit run.
    :ivar dist_drill_rot: Distance drilled - rotating.
    :ivar dist_drill_slid: Distance drilled - sliding
    :ivar dist_ream: Distance reamed.
    :ivar dist_hold: Distance covered while holding angle with a
        steerable drilling assembly.
    :ivar dist_steering: Distance covered while actively steering with a
        steerable drilling assembly.
    :ivar rpm_av: Average turn rate (commonly in rpm) through Interval.
    :ivar rpm_mx: Maximum turn rate (commonly in rpm).
    :ivar rpm_mn: Minimum turn rate (commonly in rpm).
    :ivar rpm_av_dh: Average turn rate (commonly in rpm) downhole.
    :ivar rop_av: Average rate of penetration through Interval.
    :ivar rop_mx: Maximum rate of penetration through Interval.
    :ivar rop_mn: Minimum rate of penetration through Interval.
    :ivar wob_av: Surface weight on bit - average through interval.
    :ivar wob_mx: Weight on bit - maximum.
    :ivar wob_mn: Weight on bit - minimum.
    :ivar wob_av_dh: Weight on bit - average downhole.
    :ivar reason_trip: Reason for trip.
    :ivar objective_bha: Objective of bottom hole assembly.
    :ivar azi_top: Azimuth at start measured depth.
    :ivar azi_bottom: Azimuth at stop measured depth.
    :ivar incl_start: Inclination at start measured depth.
    :ivar incl_mx: Maximum inclination.
    :ivar incl_mn: Minimum inclination.
    :ivar incl_stop: Inclination at stop measured depth.
    :ivar temp_mud_dh_mx: Maximum mud temperature downhole during run.
    :ivar pres_pump_av: Average pump pressure.
    :ivar flowrate_bit: Flow rate at bit.
    :ivar mud_class: The class of the drilling fluid.
    :ivar mud_sub_class: Mud Subtype at event occurrence.
    :ivar comments: Comments and remarks.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar tubular: A pointer to the tubular assembly.
    :ivar uid: Unique identifier for the parameters
    """
    etim_op_bit: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "ETimOpBit",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    md_hole_start: Optional[MeasuredDepth] = field(
        default=None,
        metadata={
            "name": "MdHoleStart",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    md_hole_stop: Optional[MeasuredDepth] = field(
        default=None,
        metadata={
            "name": "MdHoleStop",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    hkld_rot: Optional[ForceMeasure] = field(
        default=None,
        metadata={
            "name": "HkldRot",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    over_pull: Optional[ForceMeasure] = field(
        default=None,
        metadata={
            "name": "OverPull",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    slack_off: Optional[ForceMeasure] = field(
        default=None,
        metadata={
            "name": "SlackOff",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    hkld_up: Optional[ForceMeasure] = field(
        default=None,
        metadata={
            "name": "HkldUp",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    hkld_dn: Optional[ForceMeasure] = field(
        default=None,
        metadata={
            "name": "HkldDn",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    tq_on_bot_av: Optional[MomentOfForceMeasure] = field(
        default=None,
        metadata={
            "name": "TqOnBotAv",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    tq_on_bot_mx: Optional[MomentOfForceMeasure] = field(
        default=None,
        metadata={
            "name": "TqOnBotMx",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    tq_on_bot_mn: Optional[MomentOfForceMeasure] = field(
        default=None,
        metadata={
            "name": "TqOnBotMn",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    tq_off_bot_av: Optional[MomentOfForceMeasure] = field(
        default=None,
        metadata={
            "name": "TqOffBotAv",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    tq_dh_av: Optional[MomentOfForceMeasure] = field(
        default=None,
        metadata={
            "name": "TqDhAv",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    wt_above_jar: Optional[ForceMeasure] = field(
        default=None,
        metadata={
            "name": "WtAboveJar",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    wt_below_jar: Optional[ForceMeasure] = field(
        default=None,
        metadata={
            "name": "WtBelowJar",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    wt_mud: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "WtMud",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    flowrate_pump_av: Optional[VolumePerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "FlowratePumpAv",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    flowrate_pump_mx: Optional[VolumePerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "FlowratePumpMx",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    flowrate_pump_mn: Optional[VolumePerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "FlowratePumpMn",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    vel_nozzle_av: Optional[LengthPerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "VelNozzleAv",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pow_bit: Optional[PowerMeasure] = field(
        default=None,
        metadata={
            "name": "PowBit",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pres_drop_bit: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "PresDropBit",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    ctim_hold: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "CTimHold",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    ctim_steering: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "CTimSteering",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    ctim_drill_rot: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "CTimDrillRot",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    ctim_drill_slid: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "CTimDrillSlid",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    ctim_circ: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "CTimCirc",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    ctim_ream: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "CTimReam",
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
    rpm_av: Optional[AngularVelocityMeasure] = field(
        default=None,
        metadata={
            "name": "RpmAv",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    rpm_mx: Optional[AngularVelocityMeasure] = field(
        default=None,
        metadata={
            "name": "RpmMx",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    rpm_mn: Optional[AngularVelocityMeasure] = field(
        default=None,
        metadata={
            "name": "RpmMn",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    rpm_av_dh: Optional[AngularVelocityMeasure] = field(
        default=None,
        metadata={
            "name": "RpmAvDh",
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
    rop_mx: Optional[LengthPerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "RopMx",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    rop_mn: Optional[LengthPerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "RopMn",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    wob_av: Optional[ForceMeasure] = field(
        default=None,
        metadata={
            "name": "WobAv",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    wob_mx: Optional[ForceMeasure] = field(
        default=None,
        metadata={
            "name": "WobMx",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    wob_mn: Optional[ForceMeasure] = field(
        default=None,
        metadata={
            "name": "WobMn",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    wob_av_dh: Optional[ForceMeasure] = field(
        default=None,
        metadata={
            "name": "WobAvDh",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    reason_trip: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReasonTrip",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 2000,
        }
    )
    objective_bha: Optional[str] = field(
        default=None,
        metadata={
            "name": "ObjectiveBha",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 2000,
        }
    )
    azi_top: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "AziTop",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    azi_bottom: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "AziBottom",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    incl_start: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "InclStart",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    incl_mx: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "InclMx",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    incl_mn: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "InclMn",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    incl_stop: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "InclStop",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    temp_mud_dh_mx: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "TempMudDhMx",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pres_pump_av: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "PresPumpAv",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    flowrate_bit: Optional[VolumePerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "FlowrateBit",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    mud_class: Optional[MudType] = field(
        default=None,
        metadata={
            "name": "MudClass",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    mud_sub_class: Optional[MudSubType] = field(
        default=None,
        metadata={
            "name": "MudSubClass",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    comments: Optional[str] = field(
        default=None,
        metadata={
            "name": "Comments",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 2000,
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
    tubular: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Tubular",
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
