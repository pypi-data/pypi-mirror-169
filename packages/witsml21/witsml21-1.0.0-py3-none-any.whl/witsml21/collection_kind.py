from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class CollectionKind(Enum):
    """
    The list of enumerated values for a collection.
    """
    FOLDER = "folder"
    PROJECT = "project"
    REALIZATION = "realization"
    SCENARIO = "scenario"
    STUDY = "study"
