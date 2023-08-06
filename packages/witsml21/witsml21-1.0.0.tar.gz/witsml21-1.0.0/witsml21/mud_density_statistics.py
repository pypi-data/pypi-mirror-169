from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.data_object_reference import DataObjectReference
from witsml21.mass_per_volume_measure import MassPerVolumeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class MudDensityStatistics:
    """
    Mud density readings at average or channel.

    :ivar average: Average mud density through the interval.
    :ivar channel: Log channel from which the mud density statistics
        were calculated.
    """
    average: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "Average",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    channel: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Channel",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
