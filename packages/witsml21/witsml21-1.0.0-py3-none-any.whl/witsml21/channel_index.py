from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from witsml21.abstract_interval import AbstractInterval
from witsml21.data_index_kind import DataIndexKind
from witsml21.data_object_reference import DataObjectReference
from witsml21.index_direction import IndexDirection
from witsml21.legacy_unit_of_measure import LegacyUnitOfMeasure
from witsml21.unit_of_measure import UnitOfMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class ChannelIndex:
    """
    Common information about a primary or secondary index for a channel or
    channel set.

    :ivar index_kind: The kind of index (date time, measured depth,
        etc.). IMMUTABLE. Set on object creation and MUST NOT change
        thereafter. Customer provided changes after creation are an
        error.
    :ivar index_property_kind: An optional value pointing to a
        PropertyKind. Energistics provides a list of standard property
        kinds that represent the basis for the commonly used properties
        in the E&amp;P subsurface workflow. This PropertyKind
        enumeration is in the external PropertyKindDictionary XML file
        in the Common ancillary folder. IMMUTABLE. Set on object
        creation and MUST NOT change thereafter. Customer provided
        changes after creation are an error.
    :ivar uom: The unit of measure of the index. Must be one of the
        units allowed for the specified IndexKind (e.g., time or depth).
        IMMUTABLE. Set on object creation and MUST NOT change
        thereafter. Customer provided changes after creation are an
        error.
    :ivar direction: The direction of the index, either increasing or
        decreasing. Index direction may not change within the life of a
        channel or channel set. This only affects the order in which
        data is streamed or serialized. IMMUTABLE. Set on object
        creation and MUST NOT change thereafter. Customer provided
        changes after creation are an error.
    :ivar mnemonic: The mnemonic for the index. IMMUTABLE. Set on object
        creation and MUST NOT change thereafter. Customer provided
        changes after creation are an error.
    :ivar datum: For depth indexes, this is a pointer to the reference
        point defining the vertical datum, in a channel's Well object,
        to which all of the index values are referenced. IMMUTABLE. Set
        on object creation and MUST NOT change thereafter. Customer
        provided changes after creation are an error.
    :ivar index_interval: The index value range for this index for the
        channel or channel set. This MUST reflect the minimum and
        maximum index values for this index for data points in the
        channel or channel set. This is independent of the direction for
        the primary index. This MUST be specified when there are data
        points in the channel or channel set, and it MUST NOT be
        specified when there are no data points in the channel or
        channel set. STORE MANAGED. This is populated by a store on
        read. Customer provided values are ignored on write
    """
    index_kind: Optional[DataIndexKind] = field(
        default=None,
        metadata={
            "name": "IndexKind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    index_property_kind: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "IndexPropertyKind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    uom: Optional[Union[LegacyUnitOfMeasure, UnitOfMeasure, str]] = field(
        default=None,
        metadata={
            "name": "Uom",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "pattern": r".*:.*",
        }
    )
    direction: Optional[IndexDirection] = field(
        default=None,
        metadata={
            "name": "Direction",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
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
    datum: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Datum",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
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
