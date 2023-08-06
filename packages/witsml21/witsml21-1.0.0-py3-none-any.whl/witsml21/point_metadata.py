from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional, Union
from witsml21.channel_data_kind import ChannelDataKind
from witsml21.data_object_reference import DataObjectReference
from witsml21.legacy_unit_of_measure import LegacyUnitOfMeasure
from witsml21.log_channel_axis import LogChannelAxis
from witsml21.unit_of_measure import UnitOfMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class PointMetadata:
    """Used to declare that data points in a specific WITSML log channel may
    contain value attributes (e.g., quality identifiers).

    This declaration is independent from the possibility that ETP may
    have sent ValueAttributes in real time. If an instance of
    PointMetadata is present for a Channel, then the value for that
    point is represented as an array in the bulk data string.

    :ivar name: The name of the point metadata. IMMUTABLE. Set on object
        creation and MUST NOT change thereafter. Customer provided
        changes after creation are an error.
    :ivar data_kind: The kind of point metadata. IMMUTABLE. Set on
        object creation and MUST NOT change thereafter. Customer
        provided changes after creation are an error.
    :ivar description: Free format description of the point metadata.
    :ivar uom: The underlying unit of measure of the value. IMMUTABLE.
        Set on object creation and MUST NOT change thereafter. Customer
        provided changes after creation are an error.
    :ivar metadata_property_kind: An optional value pointing to a
        PropertyKind. Energistics provides a list of standard property
        kinds that represent the basis for the commonly used properties
        in the E&amp;P subsurface workflow. This PropertyKind
        enumeration is in the external PropertyKindDictionary XML file
        in the Common ancillary folder. IMMUTABLE. Set on object
        creation and MUST NOT change thereafter. Customer provided
        changes after creation are an error.
    :ivar axis_definition: IMMUTABLE. Set on object creation and MUST
        NOT change thereafter. Customer provided changes after creation
        are an error. IMMUTABLE. Set on object creation and MUST NOT
        change thereafter. Customer provided changes after creation are
        an error.
    :ivar datum: Defines a vertical datum that point metadata values
        that are measured depth or vertical depth values are referenced
        to. IMMUTABLE. Set on object creation and MUST NOT change
        thereafter. Customer provided changes after creation are an
        error.
    """
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    data_kind: Optional[ChannelDataKind] = field(
        default=None,
        metadata={
            "name": "DataKind",
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
            "required": True,
            "max_length": 2000,
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
    metadata_property_kind: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "MetadataPropertyKind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    axis_definition: List[LogChannelAxis] = field(
        default_factory=list,
        metadata={
            "name": "AxisDefinition",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
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
