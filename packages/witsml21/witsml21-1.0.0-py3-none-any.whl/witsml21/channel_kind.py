from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.abstract_object import AbstractObject
from witsml21.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class ChannelKind(AbstractObject):
    """Common information about a kind of channel, such as channels produced by
    a sensor on a specific type of equipment.

    For example, a kind could represent the gamma ray channels from a
    specific gamma ray logging tool from a specific logging company.

    :ivar logging_company_name: Name of the logging company that creates
        this kind of channel.
    :ivar logging_company_code: The RP66 organization code assigned to
        the logging company. The list is available at
        http://www.energistics.org/geosciences/geology-
        standards/rp66-organization-codes
    :ivar mnemonic: The mnemonic for this kind of channel.
    :ivar property_kind: The kind of property for this kind of channel.
    :ivar mnemonic_lis: The LIS mnemonic for this kind of channel.
    :ivar logging_tool_kind: The kind of logging tool that creates this
        kind of channel.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/witsmlv2"

    logging_company_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "LoggingCompanyName",
            "type": "Element",
            "required": True,
            "max_length": 256,
        }
    )
    logging_company_code: Optional[int] = field(
        default=None,
        metadata={
            "name": "LoggingCompanyCode",
            "type": "Element",
            "required": True,
        }
    )
    mnemonic: Optional[str] = field(
        default=None,
        metadata={
            "name": "Mnemonic",
            "type": "Element",
            "required": True,
            "max_length": 64,
        }
    )
    property_kind: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "PropertyKind",
            "type": "Element",
            "required": True,
        }
    )
    mnemonic_lis: Optional[str] = field(
        default=None,
        metadata={
            "name": "MnemonicLIS",
            "type": "Element",
            "max_length": 64,
        }
    )
    logging_tool_kind: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "LoggingToolKind",
            "type": "Element",
        }
    )
