from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.abstract_temperature_pressure import AbstractTemperaturePressure
from witsml21.mass_per_volume_measure import MassPerVolumeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class DensityValue:
    """
    A possibly temperature and pressure corrected desity value.

    :ivar density: The density of the product.
    :ivar measurement_pressure_temperature:
    """
    density: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "Density",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    measurement_pressure_temperature: Optional[AbstractTemperaturePressure] = field(
        default=None,
        metadata={
            "name": "MeasurementPressureTemperature",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
        }
    )
