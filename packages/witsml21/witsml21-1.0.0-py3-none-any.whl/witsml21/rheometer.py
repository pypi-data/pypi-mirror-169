from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.extension_name_value import ExtensionNameValue
from witsml21.pressure_measure import PressureMeasure
from witsml21.rheometer_viscosity import RheometerViscosity
from witsml21.thermodynamic_temperature_measure import ThermodynamicTemperatureMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class Rheometer:
    """Rheometer readings taken during a drill report period.

    A rheometer is viscosimeter use for some fluid measurements,
    particularly when solid suspension properties are needed.

    :ivar temp_rheom: Rheometer temperature.
    :ivar pres_rheom: Rheometer pressure.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar viscosity:
    :ivar uid: Unique identifier for this instance of Rheometer.
    """
    temp_rheom: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "TempRheom",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pres_rheom: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "PresRheom",
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
    viscosity: List[RheometerViscosity] = field(
        default_factory=list,
        metadata={
            "name": "Viscosity",
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
