from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class GasPeakType(Enum):
    """
    Type of gas reading.
    """
    CIRCULATING_BACKGROUND_GAS = "circulating background gas"
    CONNECTION_GAS = "connection gas"
    DRILLING_BACKGROUND_GAS = "drilling background gas"
    DRILLING_GAS_PEAK = "drilling gas peak"
    FLOW_CHECK_GAS = "flow check gas"
    NO_READINGS = "no readings"
    OTHER = "other"
    SHUT_DOWN_GAS = "shut down gas"
    TRIP_GAS = "trip gas"
