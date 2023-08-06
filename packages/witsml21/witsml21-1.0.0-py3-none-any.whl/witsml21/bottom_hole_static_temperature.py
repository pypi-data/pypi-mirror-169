from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.abstract_bottom_hole_temperature import AbstractBottomHoleTemperature
from witsml21.time_measure import TimeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class BottomHoleStaticTemperature(AbstractBottomHoleTemperature):
    """
    Static temperature at the bottom of the hole.

    :ivar etim_static: Elapsed time since circulation stopped.
    """
    etim_static: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "ETimStatic",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
