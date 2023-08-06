from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.force_measure_ext import ForceMeasureExt
from witsml21.force_parameter_kind import ForceParameterKind
from witsml21.mud_log_parameter import MudLogParameter

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class MudLogForceParameter(MudLogParameter):
    value: Optional[ForceMeasureExt] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    force_parameter_kind: Optional[ForceParameterKind] = field(
        default=None,
        metadata={
            "name": "ForceParameterKind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
