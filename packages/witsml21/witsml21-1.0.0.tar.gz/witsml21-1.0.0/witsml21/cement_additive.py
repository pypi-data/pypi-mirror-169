from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.extension_name_value import ExtensionNameValue
from witsml21.mass_measure import MassMeasure
from witsml21.mass_per_volume_measure import MassPerVolumeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class CementAdditive:
    """
    Cement Additive Component Schema.

    :ivar name_add: Additive name.
    :ivar type_add: Additive type or function (e.g., retarder,
        visosifier, weighting agent).
    :ivar form_add: Wet or dry.
    :ivar dens_add: Additive density.
    :ivar additive: Additive amount.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar uid: Unique identifier for the additive.
    """
    name_add: Optional[str] = field(
        default=None,
        metadata={
            "name": "NameAdd",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    type_add: Optional[str] = field(
        default=None,
        metadata={
            "name": "TypeAdd",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    form_add: Optional[str] = field(
        default=None,
        metadata={
            "name": "FormAdd",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    dens_add: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "DensAdd",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    additive: Optional[MassMeasure] = field(
        default=None,
        metadata={
            "name": "Additive",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    extension_name_value: List[ExtensionNameValue] = field(
        default_factory=list,
        metadata={
            "name": "ExtensionNameValue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    uid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 64,
        }
    )
