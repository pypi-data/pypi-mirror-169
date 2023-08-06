from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class StimFetTestAnalysisMethod(Enum):
    """
    Specifies the types of stimulation FET analysis methods.
    """
    AVERAGE = "average"
    DELTA_PRESSURE_OVER_G_TIME = "delta pressure over g-time"
    DELTA_PRESSURE_OVER_LINEAR_TIME = "delta pressure over linear time"
    DELTA_PRESSURE_OVER_RADIAL_TIME = "delta pressure over radial time"
    GDK_2_D = "gdk 2-d"
    HORNER = "horner"
    LINEAR = "linear"
    LOG_LOG = "log-log"
    NOLTE = "nolte"
    OTHER = "other"
    PDL_COEFFICIENT = "pdl coefficient"
    PERKINS_AND_KERN_2_D = "perkins and kern 2-d"
    RADIAL_2_D = "radial 2-d"
    SQUARE_ROOT = "square root"
    THIRD_PARTY_SOFTWARE = "third-party software"
