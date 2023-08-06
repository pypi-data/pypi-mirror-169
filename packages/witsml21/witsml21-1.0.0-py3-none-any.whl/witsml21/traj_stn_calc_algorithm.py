from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class TrajStnCalcAlgorithm(Enum):
    """
    Specifies the trajectory station calculation algorithm.
    """
    AVERAGE_ANGLE = "average angle"
    BALANCED_TANGENTIAL = "balanced tangential"
    CONSTANT_TOOL_FACE = "constant tool face"
    CUSTOM = "custom"
    INERTIAL = "inertial"
    MINIMUM_CURVATURE = "minimum curvature"
    RADIUS_OF_CURVATURE = "radius of curvature"
    TANGENTIAL = "tangential"
