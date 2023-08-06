from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class TypeSurveyTool(Enum):
    """
    Specifies values for the type of directional survey tool; a very generic
    classification.
    """
    GYROSCOPIC_INERTIAL = "gyroscopic inertial"
    GYROSCOPIC_MWD = "gyroscopic MWD"
    GYROSCOPIC_NORTH_SEEKING = "gyroscopic north seeking"
    MAGNETIC_MULTIPLE_SHOT = "magnetic multiple-shot"
    MAGNETIC_MWD = "magnetic MWD"
    MAGNETIC_SINGLE_SHOT = "magnetic single-shot"
