from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.linear_acceleration_measure import LinearAccelerationMeasure
from witsml21.magnetic_flux_density_measure import MagneticFluxDensityMeasure
from witsml21.plane_angle_measure import PlaneAngleMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class StnTrajValid:
    """
    Captures validation information for a survey.

    :ivar mag_total_field_calc: Calculated total intensity of the
        geomagnetic field as sum of BGGM, IFR and local field.
    :ivar mag_dip_angle_calc: Calculated magnetic dip (inclination), the
        angle between the horizontal and the geomagnetic field (positive
        down, res .001).
    :ivar grav_total_field_calc: Calculated total gravitational field.
    """
    mag_total_field_calc: Optional[MagneticFluxDensityMeasure] = field(
        default=None,
        metadata={
            "name": "MagTotalFieldCalc",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    mag_dip_angle_calc: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "MagDipAngleCalc",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    grav_total_field_calc: Optional[LinearAccelerationMeasure] = field(
        default=None,
        metadata={
            "name": "GravTotalFieldCalc",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
