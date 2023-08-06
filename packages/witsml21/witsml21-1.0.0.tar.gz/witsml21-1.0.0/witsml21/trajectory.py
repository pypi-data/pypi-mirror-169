from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional, Union
from witsml21.abstract_md_growing_object import AbstractMdGrowingObject
from witsml21.data_object_reference import DataObjectReference
from witsml21.length_measure_ext import LengthMeasureExt
from witsml21.length_per_length_measure_ext import LengthPerLengthMeasureExt
from witsml21.measured_depth import MeasuredDepth
from witsml21.north_reference_kind import NorthReferenceKind
from witsml21.plane_angle_measure_ext import PlaneAngleMeasureExt
from witsml21.traj_station_type import TrajStationType
from witsml21.traj_stn_calc_algorithm import TrajStnCalcAlgorithm
from witsml21.trajectory_osduintegration import TrajectoryOsduintegration
from witsml21.trajectory_station import TrajectoryStation
from witsml21.type_survey_tool import TypeSurveyTool

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class Trajectory(AbstractMdGrowingObject):
    """The trajectory object is used to capture information about a directional
    survey in a wellbore.

    It contains many trajectory stations to capture the information
    about individual survey points. This object is uniquely identified
    within the context of one wellbore object.

    :ivar unique_identifier: A human-readable unique identifier assigned
        to the trajectory. Similar to a UWI for a well or wellbore.
    :ivar service_company: Pointer to a BusinessAssociate representing
        the contractor who provided the service.
    :ivar dtim_traj_end: End date and time of trajectory station
        measurements. Note that this is NOT a server query parameter.
    :ivar dtim_traj_start: Start date and time of trajectory station
        measurements. Note that this is NOT a server query parameter.
    :ivar definitive: True ("true" or "1") indicates that this
        trajectory is definitive for this wellbore. False ("false" or
        "0") or not given indicates otherwise. There can only be one
        trajectory per wellbore with definitive=true and it must define
        the geometry of the whole wellbore (surface to bottom). The
        definitive trajectory may represent a composite of information
        in many other trajectories. A query requesting a subset of the
        possible information can provide a simplistic view of the
        geometry of the wellbore.
    :ivar memory: Is trajectory a result of a memory dump from a tool?
        Values are "true" (or "1") and "false" (or "0").
    :ivar final_traj: Is trajectory a final or intermediate/preliminary?
        Values are "true" (or "1") and "false" (or "0").
    :ivar default_md_datum: This also contains the default projected and
        geographic systems....
    :ivar default_tvd_datum:
    :ivar parent_trajectory:
    :ivar trajectory_station:
    :ivar wellbore:
    :ivar source_trajectory:
    :ivar survey_program:
    :ivar acquisition_remark: Remarks related to acquisition context
        which is not the same as Description, which is a summary of the
        trajectory.
    :ivar mag_decl_used: Magnetic declination used to correct a Magnetic
        North referenced azimuth to a True North azimuth.  Magnetic
        declination angles are measured positive clockwise from True
        North to Magnetic North (or negative in the anti-clockwise
        direction). To convert a Magnetic azimuth to a True North
        azimuth, the magnetic declination should be added. Starting
        value if stations have individual values.
    :ivar md_max_extrapolated: The measured depth to which the survey
        segment was extrapolated.
    :ivar md_max_measured: Measured depth within the wellbore of the
        LAST trajectory station with recorded data. If a trajectory has
        been extrapolated to a deeper depth than the last surveyed
        station then that is MdMaxExtrapolated and not MdMaxMeasured.
    :ivar md_tie_on: Tie-point depth measured along the wellbore from
        the measurement reference datum to the trajectory station -
        where tie point is the place on the originating trajectory where
        the current trajectory intersecst it.
    :ivar nominal_calc_algorithm: The nominal type of algorithm used in
        the position calculation in trajectory stations. Individual
        stations may use different algorithms.
    :ivar nominal_type_survey_tool: The nominal type of tool used for
        the trajectory station measurements. Individual stations may
        have a different tool type.
    :ivar nominal_type_traj_station: The nominal type of survey station
        for the trajectory stations. Individual stations may have a
        different type.
    :ivar trajectory_osduintegration: Information about a Trajectory
        that is relevant for OSDU integration but does not have a
        natural place in a Trajectory object.
    :ivar grid_con_used: The angle  used to correct a true north
        referenced azimuth to a grid north azimuth. WITSML follows the
        Gauss-Bomford convention in which convergence angles are
        measured positive clockwise from true north to grid north (or
        negative in the anti-clockwise direction). To convert a true
        north referenced azimuth to a grid north azimuth, the
        convergence angle must be subtracted from true north. If
        StnGridConUsed is not provided, then this value applies to all
        grid-north referenced stations.
    :ivar grid_scale_factor_used: A multiplier to change geodetic
        distances based on the Earth model (ellipsoid) to distances on
        the grid plane. This is the number which was already used to
        correct lateral distances. Provide it only if it is used in your
        trajectory stations. If StnGridScaleFactorUsed is not provided,
        then this value applies to all trajectory stations. The grid
        scale factor applies to the DispEw, DispNs and Closure elements
        on trajectory stations.
    :ivar azi_vert_sect: Azimuth used for vertical section
        plot/computations.
    :ivar disp_ns_vert_sect_orig: Origin north-south used for vertical
        section plot/computations.
    :ivar disp_ew_vert_sect_orig: Origin east-west used for vertical
        section plot/computations.
    :ivar azi_ref: Specifies the definition of north. While this is
        optional because of legacy data, it is strongly recommended that
        this always be specified.
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
    service_company: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "ServiceCompany",
            "type": "Element",
        }
    )
    dtim_traj_end: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimTrajEnd",
            "type": "Element",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    dtim_traj_start: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimTrajStart",
            "type": "Element",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    definitive: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Definitive",
            "type": "Element",
        }
    )
    memory: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Memory",
            "type": "Element",
        }
    )
    final_traj: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FinalTraj",
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
    parent_trajectory: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "ParentTrajectory",
            "type": "Element",
        }
    )
    trajectory_station: List[TrajectoryStation] = field(
        default_factory=list,
        metadata={
            "name": "TrajectoryStation",
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
    source_trajectory: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "SourceTrajectory",
            "type": "Element",
        }
    )
    survey_program: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "SurveyProgram",
            "type": "Element",
        }
    )
    acquisition_remark: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcquisitionRemark",
            "type": "Element",
            "max_length": 2000,
        }
    )
    mag_decl_used: Optional[PlaneAngleMeasureExt] = field(
        default=None,
        metadata={
            "name": "MagDeclUsed",
            "type": "Element",
        }
    )
    md_max_extrapolated: Optional[MeasuredDepth] = field(
        default=None,
        metadata={
            "name": "MdMaxExtrapolated",
            "type": "Element",
        }
    )
    md_max_measured: Optional[MeasuredDepth] = field(
        default=None,
        metadata={
            "name": "MdMaxMeasured",
            "type": "Element",
        }
    )
    md_tie_on: Optional[MeasuredDepth] = field(
        default=None,
        metadata={
            "name": "MdTieOn",
            "type": "Element",
        }
    )
    nominal_calc_algorithm: Optional[Union[TrajStnCalcAlgorithm, str]] = field(
        default=None,
        metadata={
            "name": "NominalCalcAlgorithm",
            "type": "Element",
            "pattern": r".*:.*",
        }
    )
    nominal_type_survey_tool: Optional[Union[TypeSurveyTool, str]] = field(
        default=None,
        metadata={
            "name": "NominalTypeSurveyTool",
            "type": "Element",
            "pattern": r".*:.*",
        }
    )
    nominal_type_traj_station: Optional[Union[TrajStationType, str]] = field(
        default=None,
        metadata={
            "name": "NominalTypeTrajStation",
            "type": "Element",
            "pattern": r".*:.*",
        }
    )
    trajectory_osduintegration: Optional[TrajectoryOsduintegration] = field(
        default=None,
        metadata={
            "name": "TrajectoryOSDUIntegration",
            "type": "Element",
        }
    )
    grid_con_used: Optional[PlaneAngleMeasureExt] = field(
        default=None,
        metadata={
            "name": "GridConUsed",
            "type": "Element",
        }
    )
    grid_scale_factor_used: Optional[LengthPerLengthMeasureExt] = field(
        default=None,
        metadata={
            "name": "GridScaleFactorUsed",
            "type": "Element",
        }
    )
    azi_vert_sect: Optional[PlaneAngleMeasureExt] = field(
        default=None,
        metadata={
            "name": "AziVertSect",
            "type": "Element",
        }
    )
    disp_ns_vert_sect_orig: Optional[LengthMeasureExt] = field(
        default=None,
        metadata={
            "name": "DispNsVertSectOrig",
            "type": "Element",
        }
    )
    disp_ew_vert_sect_orig: Optional[LengthMeasureExt] = field(
        default=None,
        metadata={
            "name": "DispEwVertSectOrig",
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
