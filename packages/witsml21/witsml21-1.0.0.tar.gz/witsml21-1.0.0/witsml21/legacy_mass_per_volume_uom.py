from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class LegacyMassPerVolumeUom(Enum):
    KG_SCM = "kg/scm"
    LBM_1000SCF = "lbm/1000scf"
    LBM_1_E6SCF = "lbm/1E6scf"
