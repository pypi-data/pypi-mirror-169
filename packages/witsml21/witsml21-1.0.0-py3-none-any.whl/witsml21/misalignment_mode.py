from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class MisalignmentMode(Enum):
    """
    Specifies the various misalignment maths as described in SPE-90408-MS.
    """
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
