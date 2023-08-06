from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.extension_name_value import ExtensionNameValue
from witsml21.length_measure import LengthMeasure
from witsml21.sensor import Sensor
from witsml21.thermodynamic_temperature_measure import ThermodynamicTemperatureMeasure
from witsml21.volume_per_time_measure import VolumePerTimeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class MwdTool:
    """Tubular MWD Tool Component Schema.

    Used to capture operating parameters of the MWD tool.

    :ivar flowrate_mn: Minimum flow rate.
    :ivar flowrate_mx: Maximum flow rate.
    :ivar temp_mx: Maximum Temperature.
    :ivar id_equv: Equivalent inner diameter.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar sensor:
    """
    flowrate_mn: Optional[VolumePerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "FlowrateMn",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    flowrate_mx: Optional[VolumePerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "FlowrateMx",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    temp_mx: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "TempMx",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    id_equv: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "IdEquv",
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
    sensor: List[Sensor] = field(
        default_factory=list,
        metadata={
            "name": "Sensor",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
