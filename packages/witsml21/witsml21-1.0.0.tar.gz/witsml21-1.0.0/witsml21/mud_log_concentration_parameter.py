from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.concentration_parameter_kind import ConcentrationParameterKind
from witsml21.mud_log_parameter import MudLogParameter
from witsml21.volume_per_volume_measure_ext import VolumePerVolumeMeasureExt

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class MudLogConcentrationParameter(MudLogParameter):
    value: Optional[VolumePerVolumeMeasureExt] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    concentration_parameter_kind: Optional[ConcentrationParameterKind] = field(
        default=None,
        metadata={
            "name": "ConcentrationParameterKind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
