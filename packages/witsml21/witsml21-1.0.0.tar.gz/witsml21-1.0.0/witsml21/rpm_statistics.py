from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.angular_velocity_measure import AngularVelocityMeasure
from witsml21.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class RpmStatistics:
    """
    Measurement of the average turn rate and the channel from which the data
    was calculated.

    :ivar average: Average bit turn rate through the interval.
    :ivar channel: Log channel from which the turn rate statistics were
        calculated.
    """
    average: Optional[AngularVelocityMeasure] = field(
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
