from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class ForceParameterKind(Enum):
    """
    Specifies the values for mud log parameters that are measured in units of
    force.

    :cvar OVERPULL_ON_CONNECTION: Additional hookload recorded in excess
        of static drill string weight when making a connection.
    :cvar OVERPULL_ON_TRIP: Additional hookload recorded in excess of
        static drill string weight when making a trip.
    """
    OVERPULL_ON_CONNECTION = "overpull on connection"
    OVERPULL_ON_TRIP = "overpull on trip"
