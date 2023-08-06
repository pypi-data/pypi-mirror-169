from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.abstract_interval import AbstractInterval
from witsml21.extension_name_value import ExtensionNameValue
from witsml21.generic_measure import GenericMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class DepthRegParameter:
    """
    Specifies parameters associated with the log section and includes top and
    bottom indexes, a description string, and mnemonic.

    :ivar mnemonic: A dictionary-controlled mnemonic.
    :ivar dictionary: The name or identifier of the controlling
        dictionary.
    :ivar index_interval: The index value range for the vertical region
        for which the parameter value is applicable.
    :ivar value: The value assigned to the parameter. The unit of
        measure should be consistent with the property implied by
        'mnemonic' in 'dictionary'. If the value is unitless, then use a
        unit of 'Euc'.
    :ivar description: A description or definition for the mnemonic;
        required when ../dictionary is absent.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar uid: Unique identifier for the parameter.
    """
    mnemonic: Optional[str] = field(
        default=None,
        metadata={
            "name": "Mnemonic",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    dictionary: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dictionary",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    index_interval: Optional[AbstractInterval] = field(
        default=None,
        metadata={
            "name": "IndexInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    value: Optional[GenericMeasure] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 2000,
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
