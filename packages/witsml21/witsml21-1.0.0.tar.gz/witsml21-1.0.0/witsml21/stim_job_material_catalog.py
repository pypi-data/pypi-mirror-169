from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from witsml21.stim_additive import StimAdditive
from witsml21.stim_proppant_agent import StimProppantAgent

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class StimJobMaterialCatalog:
    """A listing of materials for a particular job.

    Any stage of the stim job can reference material(s) in the catalog,
    which eliminates the need to repeat the materials for each stage.

    :ivar additives: List of additives in the catalog.
    :ivar proppant_agents: List of proppant agents in the catalog.
    """
    additives: List[StimAdditive] = field(
        default_factory=list,
        metadata={
            "name": "Additives",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    proppant_agents: List[StimProppantAgent] = field(
        default_factory=list,
        metadata={
            "name": "ProppantAgents",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
