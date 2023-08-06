from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.force_per_volume_measure_ext import ForcePerVolumeMeasureExt
from witsml21.mud_log_parameter import MudLogParameter
from witsml21.pressure_gradient_parameter_kind import PressureGradientParameterKind

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class MudLogPressureGradientParameter(MudLogParameter):
    """
    Describes the kind and value of mud log parameters that are expressed in
    units of pressure gradient.

    :ivar value: The value of the parameter in pressure gradient units.
    :ivar pressure_gradient_parameter_kind:
    """
    value: Optional[ForcePerVolumeMeasureExt] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    pressure_gradient_parameter_kind: Optional[PressureGradientParameterKind] = field(
        default=None,
        metadata={
            "name": "PressureGradientParameterKind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
