from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.thermodynamic_temperature_measure import ThermodynamicTemperatureMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class AbstractBottomHoleTemperature:
    """
    One of either circulating or static temperature.

    :ivar bottom_hole_temperature: Bottomhole temperature for the job or
        reporting period.
    """
    bottom_hole_temperature: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "BottomHoleTemperature",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
