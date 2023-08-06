from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.length_measure import LengthMeasure
from witsml21.length_per_length_measure import LengthPerLengthMeasure
from witsml21.linear_acceleration_measure import LinearAccelerationMeasure
from witsml21.magnetic_flux_density_measure import MagneticFluxDensityMeasure
from witsml21.plane_angle_measure import PlaneAngleMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class StnTrajCorUsed:
    """
    Captures information about corrections applied to a trajectory station.

    :ivar grav_axial_accel_cor: Calculated gravitational field strength
        correction.
    :ivar grav_tran1_accel_cor: The correction applied to a cross-axial
        (direction 1) component of the Earth's gravitational field.
    :ivar grav_tran2_accel_cor: The correction applied to a cross-axial
        (direction 2) component of the Earth's gravitational field.
    :ivar mag_axial_drlstr_cor: Axial magnetic drill string correction.
    :ivar mag_tran1_drlstr_cor: Cross-axial (direction 1) magnetic
        correction.
    :ivar mag_tran2_drlstr_cor: Cross-axial (direction 2) magnetic
        correction.
    :ivar mag_tran1_msacor: Cross-axial (direction 1) magnetic
        correction due to a multi-station analysis process.
    :ivar mag_tran2_msacor: Cross-axial (direction 2) magnetic
        correction due to a multi-station analysis process.
    :ivar mag_axial_msacor: Axial magnetic correction due to a multi-
        station analysis process.
    :ivar sag_inc_cor: Calculated sag correction to the inclination.
    :ivar sag_azi_cor: Calculated cosag correction to the azimuth.
    :ivar stn_mag_decl_used: Magnetic declination used to correct a
        Magnetic North referenced azimuth to a True North azimuth.
        Magnetic declination angles are measured positive clockwise from
        True North to Magnetic North (or negative in the anti-clockwise
        direction). To convert a Magnetic azimuth to a True North
        azimuth, the magnetic declination should be added.
    :ivar stn_grid_con_used: The angle  used to correct a true north
        referenced azimuth to a grid north azimuth. WITSML follows the
        Gauss-Bomford convention in which convergence angles are
        measured positive clockwise from true north to grid north (or
        negative in the anti-clockwise direction). To convert a true
        north referenced azimuth to a grid north azimuth, the
        convergence angle must be subtracted from true north. If this
        value is not provided, then GridConUsed applies to all grid-
        north referenced stations.
    :ivar stn_grid_scale_factor_used: A multiplier to change geodetic
        distances based on the Earth model (ellipsoid) to distances on
        the grid plane. This is the number which was already used to
        correct lateral distances. Provide it only if it is used in your
        trajectory stations. If StnGridScaleFactorUsed is not provided,
        then the value in the parent Trajectory applies to all
        trajectory stations. The grid scale factor applies to the
        DispEw, DispNs and Closure elements on trajectory stations.
    :ivar dir_sensor_offset: Offset relative to the bit.
    """
    grav_axial_accel_cor: Optional[LinearAccelerationMeasure] = field(
        default=None,
        metadata={
            "name": "GravAxialAccelCor",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    grav_tran1_accel_cor: Optional[LinearAccelerationMeasure] = field(
        default=None,
        metadata={
            "name": "GravTran1AccelCor",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    grav_tran2_accel_cor: Optional[LinearAccelerationMeasure] = field(
        default=None,
        metadata={
            "name": "GravTran2AccelCor",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    mag_axial_drlstr_cor: Optional[MagneticFluxDensityMeasure] = field(
        default=None,
        metadata={
            "name": "MagAxialDrlstrCor",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    mag_tran1_drlstr_cor: Optional[MagneticFluxDensityMeasure] = field(
        default=None,
        metadata={
            "name": "MagTran1DrlstrCor",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    mag_tran2_drlstr_cor: Optional[MagneticFluxDensityMeasure] = field(
        default=None,
        metadata={
            "name": "MagTran2DrlstrCor",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    mag_tran1_msacor: Optional[MagneticFluxDensityMeasure] = field(
        default=None,
        metadata={
            "name": "MagTran1MSACor",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    mag_tran2_msacor: Optional[MagneticFluxDensityMeasure] = field(
        default=None,
        metadata={
            "name": "MagTran2MSACor",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    mag_axial_msacor: Optional[MagneticFluxDensityMeasure] = field(
        default=None,
        metadata={
            "name": "MagAxialMSACor",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    sag_inc_cor: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "SagIncCor",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    sag_azi_cor: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "SagAziCor",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    stn_mag_decl_used: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "StnMagDeclUsed",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    stn_grid_con_used: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "StnGridConUsed",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    stn_grid_scale_factor_used: Optional[LengthPerLengthMeasure] = field(
        default=None,
        metadata={
            "name": "StnGridScaleFactorUsed",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    dir_sensor_offset: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "DirSensorOffset",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
