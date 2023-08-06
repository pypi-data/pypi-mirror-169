from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class ChannelDerivation(Enum):
    """
    Specifies the source of data in a channel.

    :cvar RAW: Raw measured data, directly from sensors.
    :cvar SIMULATED: Simulated.
    :cvar SPLICED: Derived by splicing values from two or more other
        channels.
    :cvar SAMPLED: Derived by sampling values from one or more other
        channels.
    :cvar MODEL: Based on some modeled results of values in another one
        or more channels.
    :cvar INTERPRETED: Interpreted results of values in another one or
        more channels.
    :cvar CORRECTED: Values that have been environmentally corrected.
    :cvar EDITED: Values that have undergone depth shift, merge or other
        operations.
    """
    RAW = "raw"
    SIMULATED = "simulated"
    SPLICED = "spliced"
    SAMPLED = "sampled"
    MODEL = "model"
    INTERPRETED = "interpreted"
    CORRECTED = "corrected"
    EDITED = "edited"
