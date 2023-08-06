from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.geochronological_rank import GeochronologicalRank

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class GeochronologicalUnit:
    """A unit of geological time that can be used as part of an interpretation
    of a geology sequence.

    Use it for major units of geological time such as "Paleozoic",
    "Mesozoic" or for more detailed time intervals such as "Permian",
    "Triassic", "Jurassic", etc.

    :ivar value:
    :ivar authority: Person or collective body responsible for
        authorizing the information.
    :ivar kind: Defines the time spans in geochronology.
    """
    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 64,
        }
    )
    authority: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 64,
        }
    )
    kind: Optional[GeochronologicalRank] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
