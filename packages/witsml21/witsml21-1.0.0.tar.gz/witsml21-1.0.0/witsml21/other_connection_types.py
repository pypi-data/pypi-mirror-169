from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class OtherConnectionTypes(Enum):
    """
    Specifies the values for other types of connections.
    """
    CEMENTED_IN_PLACE = "cemented-in-place"
    DOGSCOMPRESSIONFIT_SEALED = "dogscompressionfit-sealed"
