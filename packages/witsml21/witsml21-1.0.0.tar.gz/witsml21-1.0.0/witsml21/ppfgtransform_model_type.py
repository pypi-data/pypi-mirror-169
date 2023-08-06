from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class PpfgtransformModelType(Enum):
    """
    Empirical calibrated models used for pressure calculations from a
    petrophysical channel (sonic or resistivity).
    """
    APPARENT_POISSON_S_RATIO = "apparent poisson's ratio"
    BOWERS = "bowers"
    DIAGENETIC = "diagenetic"
    EATON = "eaton"
    EATON_DAINES = "eaton-daines"
    EQUIVALENT_DEPTH = "equivalent depth"
    K0 = "k0"
    STRESS_PATH = "stress path"
