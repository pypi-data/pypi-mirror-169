from __future__ import annotations
from dataclasses import dataclass
from witsml21.abstract_cement_stage import AbstractCementStage

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class CementStageDesign(AbstractCementStage):
    """
    Configuration and other information about the cement stage.
    """
