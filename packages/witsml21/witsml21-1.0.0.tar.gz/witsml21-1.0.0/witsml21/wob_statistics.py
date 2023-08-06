from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.data_object_reference import DataObjectReference
from witsml21.force_measure import ForceMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class WobStatistics:
    """
    Measurement of average weight on bit and channel from which the data was
    calculated.

    :ivar average: Average weight on bit through the interval.
    :ivar channel: Log channel from which the WOB statistics were
        calculated.
    """
    average: Optional[ForceMeasure] = field(
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
