from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.abstract_md_interval_growing_part import AbstractMdIntervalGrowingPart
from witsml21.show_fluid import ShowFluid
from witsml21.show_rating import ShowRating
from witsml21.time_measure import TimeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class ShowEvaluationInterval(AbstractMdIntervalGrowingPart):
    """An interpretation of the overall hydrocarbon show derived from analysis
    of individual show tests on cuttings samples.

    An interval in the wellbore for which data is manually entered by
    the wellsite geologist or mud logger as an interpretation of the
    hydrocarbon show along the wellbore, based on the raw readings from
    one or more show analyses of individual show tests on cuttings
    samples. These intervals can be sent via ETP using the GrowingObject
    protocol.

    :ivar show_fluid: Gas or oil exhibited at the show interval.
    :ivar show_rating: Quality of the fluid showing at this interval.
    :ivar bottoms_up_time: Time required for a sample to leave the
        bottomhole and reach the surface.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/witsmlv2"

    show_fluid: Optional[ShowFluid] = field(
        default=None,
        metadata={
            "name": "ShowFluid",
            "type": "Element",
            "required": True,
        }
    )
    show_rating: Optional[ShowRating] = field(
        default=None,
        metadata={
            "name": "ShowRating",
            "type": "Element",
        }
    )
    bottoms_up_time: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "BottomsUpTime",
            "type": "Element",
            "required": True,
        }
    )
