from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional, Union
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
class TrajectoryReport:
    """
    Captures information for a report including trajectory stations.

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
    :ivar trajectory_station:
    """
    acquisition_remark: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcquisitionRemark",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 2000,
        }
    )
    mag_decl_used: Optional[PlaneAngleMeasureExt] = field(
        default=None,
        metadata={
            "name": "MagDeclUsed",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    md_max_extrapolated: Optional[MeasuredDepth] = field(
        default=None,
        metadata={
            "name": "MdMaxExtrapolated",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    md_max_measured: Optional[MeasuredDepth] = field(
        default=None,
        metadata={
            "name": "MdMaxMeasured",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    md_tie_on: Optional[MeasuredDepth] = field(
        default=None,
        metadata={
            "name": "MdTieOn",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    nominal_calc_algorithm: Optional[Union[TrajStnCalcAlgorithm, str]] = field(
        default=None,
        metadata={
            "name": "NominalCalcAlgorithm",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".*:.*",
        }
    )
    nominal_type_survey_tool: Optional[Union[TypeSurveyTool, str]] = field(
        default=None,
        metadata={
            "name": "NominalTypeSurveyTool",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".*:.*",
        }
    )
    nominal_type_traj_station: Optional[Union[TrajStationType, str]] = field(
        default=None,
        metadata={
            "name": "NominalTypeTrajStation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".*:.*",
        }
    )
    trajectory_osduintegration: Optional[TrajectoryOsduintegration] = field(
        default=None,
        metadata={
            "name": "TrajectoryOSDUIntegration",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    grid_con_used: Optional[PlaneAngleMeasureExt] = field(
        default=None,
        metadata={
            "name": "GridConUsed",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    grid_scale_factor_used: Optional[LengthPerLengthMeasureExt] = field(
        default=None,
        metadata={
            "name": "GridScaleFactorUsed",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    azi_vert_sect: Optional[PlaneAngleMeasureExt] = field(
        default=None,
        metadata={
            "name": "AziVertSect",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    disp_ns_vert_sect_orig: Optional[LengthMeasureExt] = field(
        default=None,
        metadata={
            "name": "DispNsVertSectOrig",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    disp_ew_vert_sect_orig: Optional[LengthMeasureExt] = field(
        default=None,
        metadata={
            "name": "DispEwVertSectOrig",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    azi_ref: Optional[NorthReferenceKind] = field(
        default=None,
        metadata={
            "name": "AziRef",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    trajectory_station: List[TrajectoryStation] = field(
        default_factory=list,
        metadata={
            "name": "TrajectoryStation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
