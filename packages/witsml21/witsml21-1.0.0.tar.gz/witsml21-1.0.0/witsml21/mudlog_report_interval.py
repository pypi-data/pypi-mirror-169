from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.abstract_md_interval_growing_part import AbstractMdIntervalGrowingPart
from witsml21.chromatograph import Chromatograph
from witsml21.cuttings_geology_interval import CuttingsGeologyInterval
from witsml21.drilling_parameters import DrillingParameters
from witsml21.interpreted_geology_interval import InterpretedGeologyInterval
from witsml21.mud_gas import MudGas
from witsml21.show_evaluation_interval import ShowEvaluationInterval
from witsml21.time_measure import TimeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class MudlogReportInterval(AbstractMdIntervalGrowingPart):
    """
    The interval at which the report on the mud log was taken, detailing
    cuttings, interpreted geology, and show evaluation.

    :ivar cuttings_geology_interval: The cuttings geology interval that
        is part of this mud log report.
    :ivar interpreted_geology_interval: The interpreted geology interval
        that is part of this mud log report.
    :ivar show_evaluation_interval: The show evaluation interval that is
        part of this mud log report.
    :ivar bottoms_up_time: Time required for a sample to leave the
        bottomhole and reach the surface.
    :ivar chromatograph:
    :ivar drilling_parameters:
    :ivar mud_gas:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/witsmlv2"

    cuttings_geology_interval: Optional[CuttingsGeologyInterval] = field(
        default=None,
        metadata={
            "name": "CuttingsGeologyInterval",
            "type": "Element",
        }
    )
    interpreted_geology_interval: Optional[InterpretedGeologyInterval] = field(
        default=None,
        metadata={
            "name": "InterpretedGeologyInterval",
            "type": "Element",
        }
    )
    show_evaluation_interval: Optional[ShowEvaluationInterval] = field(
        default=None,
        metadata={
            "name": "ShowEvaluationInterval",
            "type": "Element",
        }
    )
    bottoms_up_time: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "BottomsUpTime",
            "type": "Element",
            "required": True,
        }
    )
    chromatograph: Optional[Chromatograph] = field(
        default=None,
        metadata={
            "name": "Chromatograph",
            "type": "Element",
        }
    )
    drilling_parameters: List[DrillingParameters] = field(
        default_factory=list,
        metadata={
            "name": "DrillingParameters",
            "type": "Element",
        }
    )
    mud_gas: List[MudGas] = field(
        default_factory=list,
        metadata={
            "name": "MudGas",
            "type": "Element",
        }
    )
