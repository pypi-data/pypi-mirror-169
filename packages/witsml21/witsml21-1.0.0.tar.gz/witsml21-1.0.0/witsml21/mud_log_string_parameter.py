from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.mud_log_parameter import MudLogParameter
from witsml21.mud_log_string_parameter_kind import MudLogStringParameterKind

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class MudLogStringParameter(MudLogParameter):
    """
    Stores the values of parameters that are described by character strings.

    :ivar value: The value of the parameter as a character string.
    :ivar mud_log_string_parameter_kind:
    """
    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    mud_log_string_parameter_kind: Optional[MudLogStringParameterKind] = field(
        default=None,
        metadata={
            "name": "MudLogStringParameterKind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
