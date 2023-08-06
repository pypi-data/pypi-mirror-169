from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.abstract_md_growing_part import AbstractMdGrowingPart
from witsml21.abstract_position import AbstractPosition
from witsml21.abstract_vertical_depth import AbstractVerticalDepth
from witsml21.angle_per_length_measure import AnglePerLengthMeasure
from witsml21.data_object_reference import DataObjectReference
from witsml21.length_measure import LengthMeasure
from witsml21.linear_acceleration_measure import LinearAccelerationMeasure
from witsml21.magnetic_flux_density_measure import MagneticFluxDensityMeasure
from witsml21.plane_angle_measure import PlaneAngleMeasure
from witsml21.source_trajectory_station import SourceTrajectoryStation
from witsml21.stn_traj_cor_used import StnTrajCorUsed
from witsml21.stn_traj_matrix_cov import StnTrajMatrixCov
from witsml21.stn_traj_raw_data import StnTrajRawData
from witsml21.stn_traj_valid import StnTrajValid
from witsml21.traj_station_status import TrajStationStatus
from witsml21.traj_station_type import TrajStationType
from witsml21.traj_stn_calc_algorithm import TrajStnCalcAlgorithm
from witsml21.trajectory_station_osduintegration import TrajectoryStationOsduintegration
from witsml21.type_survey_tool import TypeSurveyTool

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class TrajectoryStation(AbstractMdGrowingPart):
    """WITSML - Trajectory Station Component Schema

    :ivar closure: The horizontal straight line distance from the
        trajectory origin (Well surface location) to this trajectory
        station, calculated using the Pythagorean Theorem from this
        trajectory station's X and Y Offsets. Closure Distance is often
        reported only once for the bottom hole location; however, the
        value stored in this attribute is the Closure Distance at this
        trajectory station. The distance is subject to distortions by
        the projection in which the closure is computed. Often referred
        to as simply "Closure" or sometimes referred to as "Horizontal
        Displacement".
    :ivar closure_direction: The direction angle, in the horizontal
        plane relative to the north reference, of the trajectory origin
        (Well surface location) to this trajectory station calculated
        using trigonometry from this trajectory station's X and Y
        Offsets. The North Reference the Trajectory's AziRef. This value
        should be a number between 0.00 and 360.00 degrees; 0.00 and
        360.00 represent North, 90.00 is East, 180.00 is South and
        270.00 is West. Sometimes referred to as "Horizontal
        Displacement Direction" or "Horizontal Displacement Bearing".
    :ivar disp_latitude: The difference between the well surface hole
        latitude and the trajectory station latitude. A positive value
        indicates a northerly direction; a negative value indicates a
        southerly direction. ADD this value to the well Surface Latitude
        to define the Station Latitude.
    :ivar disp_longitude: The difference between the well surface hole
        longitude and the trajectory station longitude. A positive value
        indicates an easterly direction; a negative value indicates a
        westerly direction. ADD this value to the well Surface Longitude
        to define the Station Longitude.
    :ivar original_latitude: The latitude of the trajectory station.
        Recommended practice is to utilize DispLatitude and
        DispLongitude instead of storing actual
        OriginalLatitude/OriginalLongitude values. NOTE - These are
        relative to the same geodetic datum as the well surface
        location.
    :ivar original_longitude: The longitude of the trajectory station.
        Recommended practice is to utilize DispLatitude and
        DispLongitude instead of storing actual
        OriginalLatitude/OriginalLongitude values. NOTE - These are
        relative to the same geodetic datum as the well surface
        location.
    :ivar trajectory_station_osduintegration: Information about a
        TrajectoryStation that is relevant for OSDU integration but does
        not have a natural place in a TrajectoryStation object.
    :ivar true_closure: The horizontal straight line distance from the
        trajectory origin (Well surface location) to this trajectory
        station, calculated using the Pythagorean Theorem from this
        trajectory station's X and Y Offsets. True Closure Distance is
        often reported only once for the bottom hole location; however,
        the value stored in this attribute is the True Closure Distance
        at this trajectory station. The distance is computed in a local
        CRS with scale factor one. Often referred to as simply "True
        Closure" or sometimes referred to as "True Horizontal
        Displacement".
    :ivar true_closure_direction: The direction angle, in the horizontal
        plane relative to the True North reference, of the trajectory
        origin (Well surface location) to this trajectory station,
        calculated using trigonometry from this trajectory station's X
        and Y Offsets. The direction is calculated in a True North
        oriented, local coordinate reference system anchored at the
        survey origin (Well surface location). This value should be a
        number between 0.00 and 360.00 degrees; 0.00 and 360.00
        represent North, 90.00 is East, 180.00 is South and 270.00 is
        West.
    :ivar wgs84_latitude: World map latitude based on WGS 84
        (EPSG:4326).
    :ivar wgs84_longitude: World map longitude based on WGS 84
        (EPSG:4326).
    :ivar manually_entered: Indicates whether the trajectory station
        information was manually entered by a human.
    :ivar target: A pointer to the intended target of this station.
    :ivar dtim_stn: Date and time the station was measured or created.
    :ivar type_traj_station: Type of survey station.
    :ivar type_survey_tool: The type of tool used for the measurements.
    :ivar calc_algorithm: The type of algorithm used in the position
        calculation.
    :ivar tvd: Vertical depth of the measurements.
    :ivar incl: Hole inclination, measured from vertical.
    :ivar azi: Hole azimuth. Corrected to wells azimuth reference.
    :ivar mtf: Toolface angle (magnetic).
    :ivar gtf: Toolface angle (gravity).
    :ivar disp_ns: North-south offset, positive to the North. This is
        relative to wellLocation with a North axis orientation of
        aziRef. If a displacement with respect to a different point is
        desired then define a localCRS and specify local coordinates in
        location.
    :ivar disp_ew: East-west offset, positive to the East. This is
        relative to wellLocation with a North axis orientation of
        aziRef. If a displacement with respect to a different point is
        desired then define a localCRS and specify local coordinates in
        location.
    :ivar vert_sect: Distance along vertical section azimuth plane.
    :ivar dls: Dogleg severity.
    :ivar rate_turn: Turn rate, radius of curvature computation.
    :ivar rate_build: Build Rate, radius of curvature computation.
    :ivar md_delta: Delta measured depth from previous station.
    :ivar tvd_delta: Delta true vertical depth from previous station.
    :ivar grav_total_uncert: Survey tool gravity uncertainty.
    :ivar dip_angle_uncert: Survey tool dip uncertainty.
    :ivar mag_total_uncert: Survey tool magnetic uncertainty.
    :ivar grav_accel_cor_used: Was an accelerometer alignment correction
        applied to survey computation? Values are "true" (or "1") and
        "false" (or "0").
    :ivar mag_xaxial_cor_used: Was a magnetometer alignment correction
        applied to survey computation? Values are "true" (or "1") and
        "false" (or "0").
    :ivar sag_cor_used: Was a bottom hole assembly sag correction
        applied to the survey computation? Values are "true" (or "1")
        and "false" (or "0").
    :ivar mag_drlstr_cor_used: Was a drillstring magnetism correction
        applied to survey computation? Values are "true" (or "1") and
        "false" (or "0").
    :ivar infield_ref_cor_used: Was an In Field Referencing (IFR)
        correction applied to the azimuth value? Values are "true" (or
        "1") and "false" (or "0"). An IFR survey measures the strength
        and direction of the Earth's magnetic field over the area of
        interest. By taking a geomagnetic modelled values away from
        these field survey results, we are left with a local crustal
        correction, which since it is assumed geological in nature, only
        varies over geological timescales. For MWD survey operations,
        these corrections are applied in addition to the geomagnetic
        model to provide accurate knowledge of the local magnetic field
        and hence to improve the accuracy of MWD magnetic azimuth
        measurements.
    :ivar interpolated_infield_ref_cor_used: Was an Interpolated In
        Field Referencing (IIFR) correction applied to the azimuth
        value? Values are "true" (or "1") and "false" (or "0").
        Interpolated In Field Referencing measures the diurnal Earth
        magnetic field variations resulting from electrical currents in
        the ionosphere and effects of magnetic storms hitting the Earth.
        It increases again the accuracy of the magnetic azimuth
        measurement.
    :ivar in_hole_ref_cor_used: Was an In Hole Referencing (IHR)
        correction applied to the inclination and/or azimuth values?
        Values are "true" (or "1") and "false" (or "0"). In-Hole
        Referencing essentially involves comparing gyro surveys to MWD
        surveys in a tangent section of a well. Once a small part of a
        tangent section has been drilled and surveyed using an MWD tool,
        then an open hole (OH) gyro is run. By comparing the Gyro
        surveys to the MWD surveys a correction can be calculated for
        the MWD. This correction is then assumed as valid for the rest
        of the tangent section allowing to have a near gyro accuracy for
        the whole section, therefore reducing the ellipse of uncertainty
        (EOU) size.
    :ivar axial_mag_interference_cor_used: Was an Axial Magnetic
        Interference (AMI) correction applied to the azimuth value?
        Values are "true" (or "1") and "false" (or "0"). Most of the
        BHAs used to drill wells include an MWD tool. An MWD is a
        magnetic survey tool and as such suffer from magnetic
        interferences from a wide variety of sources. Magnetic
        interferences can be categorized into axial and radial type
        interferences. Axial interferences are mainly the result of
        magnetic poles from the drill string steel components located
        below and above the MWD tool. Radial interferences are numerous.
        Therefore, there is a risk that magXAxialCorUsed includes both
        Axial and radial corrections.
    :ivar cosag_cor_used: WWas a Cosag Correction applied to the azimuth
        values? Values are "true" (or "1") and "false" (or "0"). The BHA
        Sag Correction is the same as the Sag Correction except it
        includes the horizontal misalignment (Cosag).
    :ivar msacor_used: Was a correction applied to the survey due to a
        Multi-Station Analysis process? Values are "true" (or "1") and
        "false" (or "0").
    :ivar grav_total_field_reference: Gravitational field
        theoretical/reference value.
    :ivar mag_total_field_reference: Geomagnetic field
        theoretical/reference value.
    :ivar mag_dip_angle_reference: Magnetic dip angle
        theoretical/reference value.
    :ivar mag_model_used: Geomagnetic model used.
    :ivar mag_model_valid: Current valid interval for the geomagnetic
        model used.
    :ivar geo_model_used: Gravitational model used.
    :ivar status_traj_station: Status of the station.
    :ivar raw_data:
    :ivar cor_used:
    :ivar valid:
    :ivar matrix_cov:
    :ivar location:
    :ivar source_station:
    :ivar tool_error_model:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/witsmlv2"

    closure: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "Closure",
            "type": "Element",
        }
    )
    closure_direction: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "ClosureDirection",
            "type": "Element",
        }
    )
    disp_latitude: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "DispLatitude",
            "type": "Element",
        }
    )
    disp_longitude: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "DispLongitude",
            "type": "Element",
        }
    )
    original_latitude: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "OriginalLatitude",
            "type": "Element",
        }
    )
    original_longitude: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "OriginalLongitude",
            "type": "Element",
        }
    )
    trajectory_station_osduintegration: Optional[TrajectoryStationOsduintegration] = field(
        default=None,
        metadata={
            "name": "TrajectoryStationOSDUIntegration",
            "type": "Element",
        }
    )
    true_closure: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "TrueClosure",
            "type": "Element",
        }
    )
    true_closure_direction: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "TrueClosureDirection",
            "type": "Element",
        }
    )
    wgs84_latitude: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "WGS84Latitude",
            "type": "Element",
        }
    )
    wgs84_longitude: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "WGS84Longitude",
            "type": "Element",
        }
    )
    manually_entered: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ManuallyEntered",
            "type": "Element",
        }
    )
    target: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Target",
            "type": "Element",
        }
    )
    dtim_stn: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimStn",
            "type": "Element",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    type_traj_station: Optional[TrajStationType] = field(
        default=None,
        metadata={
            "name": "TypeTrajStation",
            "type": "Element",
            "required": True,
        }
    )
    type_survey_tool: Optional[TypeSurveyTool] = field(
        default=None,
        metadata={
            "name": "TypeSurveyTool",
            "type": "Element",
        }
    )
    calc_algorithm: Optional[TrajStnCalcAlgorithm] = field(
        default=None,
        metadata={
            "name": "CalcAlgorithm",
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
    incl: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "Incl",
            "type": "Element",
        }
    )
    azi: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "Azi",
            "type": "Element",
        }
    )
    mtf: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "Mtf",
            "type": "Element",
        }
    )
    gtf: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "Gtf",
            "type": "Element",
        }
    )
    disp_ns: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "DispNs",
            "type": "Element",
        }
    )
    disp_ew: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "DispEw",
            "type": "Element",
        }
    )
    vert_sect: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "VertSect",
            "type": "Element",
        }
    )
    dls: Optional[AnglePerLengthMeasure] = field(
        default=None,
        metadata={
            "name": "Dls",
            "type": "Element",
        }
    )
    rate_turn: Optional[AnglePerLengthMeasure] = field(
        default=None,
        metadata={
            "name": "RateTurn",
            "type": "Element",
        }
    )
    rate_build: Optional[AnglePerLengthMeasure] = field(
        default=None,
        metadata={
            "name": "RateBuild",
            "type": "Element",
        }
    )
    md_delta: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "MdDelta",
            "type": "Element",
        }
    )
    tvd_delta: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "TvdDelta",
            "type": "Element",
        }
    )
    grav_total_uncert: Optional[LinearAccelerationMeasure] = field(
        default=None,
        metadata={
            "name": "GravTotalUncert",
            "type": "Element",
        }
    )
    dip_angle_uncert: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "DipAngleUncert",
            "type": "Element",
        }
    )
    mag_total_uncert: Optional[MagneticFluxDensityMeasure] = field(
        default=None,
        metadata={
            "name": "MagTotalUncert",
            "type": "Element",
        }
    )
    grav_accel_cor_used: Optional[bool] = field(
        default=None,
        metadata={
            "name": "GravAccelCorUsed",
            "type": "Element",
        }
    )
    mag_xaxial_cor_used: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MagXAxialCorUsed",
            "type": "Element",
        }
    )
    sag_cor_used: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SagCorUsed",
            "type": "Element",
        }
    )
    mag_drlstr_cor_used: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MagDrlstrCorUsed",
            "type": "Element",
        }
    )
    infield_ref_cor_used: Optional[bool] = field(
        default=None,
        metadata={
            "name": "InfieldRefCorUsed",
            "type": "Element",
        }
    )
    interpolated_infield_ref_cor_used: Optional[bool] = field(
        default=None,
        metadata={
            "name": "InterpolatedInfieldRefCorUsed",
            "type": "Element",
        }
    )
    in_hole_ref_cor_used: Optional[bool] = field(
        default=None,
        metadata={
            "name": "InHoleRefCorUsed",
            "type": "Element",
        }
    )
    axial_mag_interference_cor_used: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AxialMagInterferenceCorUsed",
            "type": "Element",
        }
    )
    cosag_cor_used: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CosagCorUsed",
            "type": "Element",
        }
    )
    msacor_used: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MSACorUsed",
            "type": "Element",
        }
    )
    grav_total_field_reference: Optional[LinearAccelerationMeasure] = field(
        default=None,
        metadata={
            "name": "GravTotalFieldReference",
            "type": "Element",
        }
    )
    mag_total_field_reference: Optional[MagneticFluxDensityMeasure] = field(
        default=None,
        metadata={
            "name": "MagTotalFieldReference",
            "type": "Element",
        }
    )
    mag_dip_angle_reference: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "MagDipAngleReference",
            "type": "Element",
        }
    )
    mag_model_used: Optional[str] = field(
        default=None,
        metadata={
            "name": "MagModelUsed",
            "type": "Element",
            "max_length": 64,
        }
    )
    mag_model_valid: Optional[str] = field(
        default=None,
        metadata={
            "name": "MagModelValid",
            "type": "Element",
            "max_length": 64,
        }
    )
    geo_model_used: Optional[str] = field(
        default=None,
        metadata={
            "name": "GeoModelUsed",
            "type": "Element",
            "max_length": 64,
        }
    )
    status_traj_station: Optional[TrajStationStatus] = field(
        default=None,
        metadata={
            "name": "StatusTrajStation",
            "type": "Element",
        }
    )
    raw_data: Optional[StnTrajRawData] = field(
        default=None,
        metadata={
            "name": "RawData",
            "type": "Element",
        }
    )
    cor_used: Optional[StnTrajCorUsed] = field(
        default=None,
        metadata={
            "name": "CorUsed",
            "type": "Element",
        }
    )
    valid: Optional[StnTrajValid] = field(
        default=None,
        metadata={
            "name": "Valid",
            "type": "Element",
        }
    )
    matrix_cov: Optional[StnTrajMatrixCov] = field(
        default=None,
        metadata={
            "name": "MatrixCov",
            "type": "Element",
        }
    )
    location: List[AbstractPosition] = field(
        default_factory=list,
        metadata={
            "name": "Location",
            "type": "Element",
        }
    )
    source_station: List[SourceTrajectoryStation] = field(
        default_factory=list,
        metadata={
            "name": "SourceStation",
            "type": "Element",
        }
    )
    tool_error_model: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "ToolErrorModel",
            "type": "Element",
        }
    )
