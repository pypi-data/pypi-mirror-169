from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class WellDirection(Enum):
    """
    Specifies values for the direction of flow of the fluids in a well facility
    (generally, injected or produced, or some combination).

    :cvar HUFF_N_PUFF: The well facility alternately injects (usually a
        steam or hot fluid) and produces.
    :cvar INJECTOR: The well facility is injecting fluids into the
        subsurface.
    :cvar PRODUCER: The well facility is producing fluids from the
        subsurface.
    :cvar UNCERTAIN: The flow direction of the fluids is variable, but
        not on a regular basis as is the case with the huff-n-puff flow.
    """
    HUFF_N_PUFF = "huff-n-puff"
    INJECTOR = "injector"
    PRODUCER = "producer"
    UNCERTAIN = "uncertain"
