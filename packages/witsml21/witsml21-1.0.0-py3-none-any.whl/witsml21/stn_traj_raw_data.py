from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.linear_acceleration_measure import LinearAccelerationMeasure
from witsml21.magnetic_flux_density_measure import MagneticFluxDensityMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class StnTrajRawData:
    """
    Captures raw data for a trajectory station.

    :ivar grav_axial_raw: Uncorrected gravitational field strength
        measured in the axial direction.
    :ivar grav_tran1_raw: Uncorrected gravitational field strength
        measured in the transverse direction.
    :ivar grav_tran2_raw: Uncorrected gravitational field strength
        measured in the transverse direction, approximately normal to
        tran1.
    :ivar mag_axial_raw: Uncorrected magnetic field strength measured in
        the axial direction.
    :ivar mag_tran1_raw: Uncorrected magnetic field strength measured in
        the transverse direction.
    :ivar mag_tran2_raw: Uncorrected magnetic field strength measured in
        the transverse direction, approximately normal to tran1.
    """
    grav_axial_raw: Optional[LinearAccelerationMeasure] = field(
        default=None,
        metadata={
            "name": "GravAxialRaw",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    grav_tran1_raw: Optional[LinearAccelerationMeasure] = field(
        default=None,
        metadata={
            "name": "GravTran1Raw",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    grav_tran2_raw: Optional[LinearAccelerationMeasure] = field(
        default=None,
        metadata={
            "name": "GravTran2Raw",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    mag_axial_raw: Optional[MagneticFluxDensityMeasure] = field(
        default=None,
        metadata={
            "name": "MagAxialRaw",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    mag_tran1_raw: Optional[MagneticFluxDensityMeasure] = field(
        default=None,
        metadata={
            "name": "MagTran1Raw",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    mag_tran2_raw: Optional[MagneticFluxDensityMeasure] = field(
        default=None,
        metadata={
            "name": "MagTran2Raw",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
