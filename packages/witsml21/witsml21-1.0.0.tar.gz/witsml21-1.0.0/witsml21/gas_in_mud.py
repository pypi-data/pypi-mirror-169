from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.data_object_reference import DataObjectReference
from witsml21.volume_per_volume_measure import VolumePerVolumeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class GasInMud:
    """
    Information on amount of gas in the mud.

    :ivar average: Average percentage of gas in the mud.
    :ivar maximum: Maximum percentage of gas in the mud.
    :ivar channel:
    """
    average: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "Average",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    maximum: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "Maximum",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    channel: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Channel",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
