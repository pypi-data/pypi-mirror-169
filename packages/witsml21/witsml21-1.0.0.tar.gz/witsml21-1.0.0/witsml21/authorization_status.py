from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class AuthorizationStatus(Enum):
    AGREED = "agreed"
    PROVISIONAL = "provisional"
    OBSOLETE = "obsolete"
