from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class JarType(Enum):
    """
    Specifies the type of jar.
    """
    MECHANICAL = "mechanical"
    HYDRAULIC = "hydraulic"
    HYDRO_MECHANICAL = "hydro mechanical"
