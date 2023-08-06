from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.abstract_md_interval_growing_part import AbstractMdIntervalGrowingPart
from witsml21.geochronological_unit import GeochronologicalUnit
from witsml21.interpreted_interval_lithology import InterpretedIntervalLithology
from witsml21.lithostratigraphic_unit import LithostratigraphicUnit

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class InterpretedGeologyInterval(AbstractMdIntervalGrowingPart):
    """Represents a depth interval along the wellbore which contains a single
    interpreted lithology type. It can be used to:

    - carry information about geochronology and lithostratigraphy
    - create a pre-well geological prognosis with chronostratigraphic, lithostratigraphic, and lithology entries.
    These intervals can be sent via ETP using the GrowingObject protocol.

    :ivar geochronological_unit: The name of a Geochronology, with the
        "kind" attribute specifying the geochronological time span.
    :ivar lithostratigraphic_unit: Specifies the unit of
        lithostratigraphy.
    :ivar interpreted_lithology:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/witsmlv2"

    geochronological_unit: List[GeochronologicalUnit] = field(
        default_factory=list,
        metadata={
            "name": "GeochronologicalUnit",
            "type": "Element",
        }
    )
    lithostratigraphic_unit: List[LithostratigraphicUnit] = field(
        default_factory=list,
        metadata={
            "name": "LithostratigraphicUnit",
            "type": "Element",
        }
    )
    interpreted_lithology: Optional[InterpretedIntervalLithology] = field(
        default=None,
        metadata={
            "name": "InterpretedLithology",
            "type": "Element",
        }
    )
