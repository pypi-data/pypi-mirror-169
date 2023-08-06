from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class LoggingMethod(Enum):
    """
    Specifies the method of logging used to record or produce the data in the
    log.

    :cvar COILED_TUBING: The data of the log is a result of coiled
        tubing logging.
    :cvar COMPUTED: The log is a result of computed analyses from
        various sources.
    :cvar DISTRIBUTED: The log is derived from various different
        systems.
    :cvar LWD: The data of the log is a result of logging-while-
        drilling.
    :cvar MIXED: The data is derived from multiple logging methods.
    :cvar MWD: The data of the log is a result of measurement-while-
        drilling.
    :cvar SUBSEA: The data is recorded with a subsea sensor.
    :cvar SURFACE: The data is recorded on the surface or in real time.
    :cvar WIRELINE: The data of the log is a result of wireline logging.
    """
    COILED_TUBING = "coiled tubing"
    COMPUTED = "computed"
    DISTRIBUTED = "distributed"
    LWD = "LWD"
    MIXED = "mixed"
    MWD = "MWD"
    SUBSEA = "subsea"
    SURFACE = "surface"
    WIRELINE = "wireline"
