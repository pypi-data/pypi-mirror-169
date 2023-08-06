from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional, Union
from witsml21.abstract_active_object import AbstractActiveObject
from witsml21.abstract_interval import AbstractInterval
from witsml21.channel_data import ChannelData
from witsml21.channel_data_kind import ChannelDataKind
from witsml21.channel_derivation import ChannelDerivation
from witsml21.channel_index import ChannelIndex
from witsml21.channel_osduintegration import ChannelOsduintegration
from witsml21.channel_state import ChannelState
from witsml21.data_object_reference import DataObjectReference
from witsml21.generic_measure import GenericMeasure
from witsml21.hole_logging_status import HoleLoggingStatus
from witsml21.legacy_unit_of_measure import LegacyUnitOfMeasure
from witsml21.length_measure_ext import LengthMeasureExt
from witsml21.log_channel_axis import LogChannelAxis
from witsml21.logging_method import LoggingMethod
from witsml21.logging_tool_class import LoggingToolType
from witsml21.mud_class import MudType
from witsml21.mud_sub_class import MudSubType
from witsml21.pass_detail import PassDetail
from witsml21.point_metadata import PointMetadata
from witsml21.unit_of_measure import UnitOfMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class Channel(AbstractActiveObject):
    """A channel object.

    It corresponds roughly to the LogCurveInfo structure in WITSML1411,
    and directly corresponds to the ChannelMetadataRecord structure in
    ETP. In historian terminology, a channel corresponds directly to a
    tag. Channels are the fundamental unit of organization for WITSML
    logs. BUSINESS RULE: The Uom MUST be compatible with the
    QuantityClass of the PropertyKind specified in ChannelClass.

    :ivar mnemonic: The mnemonic name for this channel. Mnemonics are
        not unique within a store. IMMUTABLE. Set on object creation and
        MUST NOT change thereafter. Customer provided changes after
        creation are an error.
    :ivar global_mnemonic: A standardized mnemonic name for this
        channel.
    :ivar data_kind: The kind of channel data value for this channel.
        IMMUTABLE. Set on object creation and MUST NOT change
        thereafter. Customer provided changes after creation are an
        error.
    :ivar uom: The underlying unit of measure of the value. IMMUTABLE.
        Set on object creation and MUST NOT change thereafter. Customer
        provided changes after creation are an error.
    :ivar source: Source of the data in the channel. Enter the
        contractor name who conducted the log.
    :ivar channel_state: Defines where the channel gets its data from,
        e.g., calculated from another source, or from archive, or raw
        real-time, etc.
    :ivar channel_property_kind: A mandatory value pointing to a
        PropertyKind. Energistics provides a list of standard property
        kinds that represent the basis for the commonly used properties
        in the E&amp;P subsurface workflow. This PropertyKind
        enumeration is in the external PropertyKindDictionary XML file
        in the Common ancillary folder.
    :ivar run_number: The nominal run number for the channel. No precise
        meaning is declared for this attribute but it is so commonly
        used that it must be included. The value here should match a bit
        run number for LWD data and a wireline run number for logging
        data.
    :ivar pass_number: The nominal pass number for the channel. No
        precise meaning is declared for this attribute but it is so
        commonly used that it must be included. The value here should
        match a wireline pass number for logging data. Use PassDetail
        instead if the channel contains information about several passes
        using PassIndexedDepth..
    :ivar pass_description: The nominal pass description for the pass
        such as Calibration Pass, Main Pass, Repeated Pass. Use
        PassDetail instead if the channel contains information about
        several passes using PassIndexedDepth.
    :ivar pass_detail: Details about one or more passes when using
        PassIndexedDepth.
    :ivar primary_index_interval: The primary index value range for the
        channel. This MUST reflect the minimum and maximum primary index
        values for data points in the channel. This is independent of
        the direction for the primary index. This MUST be specified when
        there are data points in the channel, and it MUST NOT be
        specified when there are no data points in the channel. STORE
        MANAGED. This is populated by a store on read. Customer provided
        values are ignored on write
    :ivar logging_company: Pointer to a BusinessAssociate representing
        the logging company.
    :ivar logging_company_code: The RP66 organization code assigned to a
        logging company. The list is available at
        http://www.energistics.org/geosciences/geology-
        standards/rp66-organization-codes
    :ivar channel_kind: An optional value pointing to a ChannelKind.
        Energistics provides a list of standard channel kinds from the
        Practical Well Logging Standard (PWLS). This ChannelKind
        enumeration is in the external ChannelKindDictionary XML file in
        the WITSML ancillary folder.
    :ivar logging_tool_kind: An optional value pointing to a
        LoggingToolKind. Energistics provides a list of standard logging
        tool kinds from the Practical Well Logging Standard (PWLS). This
        LoggingToolKind enumeration is in the external
        LoggingToolKindDictionary XML file in the WITSML ancillary
        folder.
    :ivar logging_tool_class: A value categorizing a logging tool. The
        classification system used in WITSML is the one from the PWLS
        group.
    :ivar derivation: Indicates how data in the channel is derived.
    :ivar logging_method: Defines where the log channel gets its data
        from: LWD, MWD, wireline; or whether it is computed, etc.
    :ivar nominal_hole_size: The nominal hole size at the time the
        measurement tool was in the hole. The size is "nominal" to
        indicate that this is not the result of a caliper reading or
        other direct measurement of the hole size, but is just a name
        used to refer to the diameter. This is normally the bit size. In
        a case where there are more than one diameter hole being drilled
        at the same time (like where a reamer is behind the bit) this
        diameter is the one which was seen by the sensor which produced
        a particular log channel.
    :ivar sensor_offset: The consistent distance from the downhole
        equipment vertical reference (the drill bit, for MWD logs; the
        tool zero reference for wireline logs) at which the channel
        values are measured or calculated. This is typically, but not
        always, the distance from the bit to the sensor. This element is
        only informative (channel values are presented at actual depth,
        not requiring subtraction of an offset).
    :ivar mud_class: The class of the drilling fluid at the time of
        logging.
    :ivar mud_sub_class: The subclass of drilling fluid at the time of
        logging.
    :ivar hole_logging_status: The status of the hole at the time of
        logging.
    :ivar is_continuous: If true, the channel data values are continues
        values, such as sampled measurement values. If false, the
        channel data values are discrete, such as rig activity codes.
    :ivar nominal_sampling_interval: For regularly sampled channel data,
        this represents the nominal sampling interval. This should not
        be set when data is not regularly sampled.
    :ivar channel_osduintegration: Information about a Channel that is
        relevant for OSDU integration but does not have a natural place
        in a Channel object.
    :ivar datum: Pointer to a reference point that defines a vertical
        datum that channel data values that are measured depth or
        vertical depth values are referenced to. This is NOT an datum
        for index values. See Datum in ChannelIndex for the datum for
        index values. IMMUTABLE. Set on object creation and MUST NOT
        change thereafter. Customer provided changes after creation are
        an error.
    :ivar seismic_reference_elevation: Pointer to a reference point that
        defines the seismic reference elevation. This should only be
        populated if the channel represents time-depth relationships or
        checkshots.
    :ivar data: STORE MANAGED. This is populated by a store on read.
        Customer provided values are ignored on write
    :ivar data_source:
    :ivar index: Defines metadata about the channel's primary and
        secondary indexes. The first index is the primary index. Any
        additional indexes are secondary indexes.
    :ivar derived_from: This element is to be used in conjunction with
        the Derivation element. When Derivation indicates that a process
        was used to generate this channel, DerivedFrom may point to the
        channel or channels used in the process of generating this
        channel.
    :ivar wellbore:
    :ivar axis_definition:
    :ivar point_metadata:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/witsmlv2"

    mnemonic: Optional[str] = field(
        default=None,
        metadata={
            "name": "Mnemonic",
            "type": "Element",
            "required": True,
            "max_length": 64,
        }
    )
    global_mnemonic: Optional[str] = field(
        default=None,
        metadata={
            "name": "GlobalMnemonic",
            "type": "Element",
            "required": True,
            "max_length": 64,
        }
    )
    data_kind: Optional[ChannelDataKind] = field(
        default=None,
        metadata={
            "name": "DataKind",
            "type": "Element",
            "required": True,
        }
    )
    uom: Optional[Union[LegacyUnitOfMeasure, UnitOfMeasure, str]] = field(
        default=None,
        metadata={
            "name": "Uom",
            "type": "Element",
            "required": True,
            "pattern": r".*:.*",
        }
    )
    source: Optional[str] = field(
        default=None,
        metadata={
            "name": "Source",
            "type": "Element",
            "max_length": 64,
        }
    )
    channel_state: Optional[ChannelState] = field(
        default=None,
        metadata={
            "name": "ChannelState",
            "type": "Element",
        }
    )
    channel_property_kind: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "ChannelPropertyKind",
            "type": "Element",
            "required": True,
        }
    )
    run_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "RunNumber",
            "type": "Element",
            "max_length": 64,
        }
    )
    pass_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "PassNumber",
            "type": "Element",
            "max_length": 64,
        }
    )
    pass_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "PassDescription",
            "type": "Element",
            "max_length": 64,
        }
    )
    pass_detail: List[PassDetail] = field(
        default_factory=list,
        metadata={
            "name": "PassDetail",
            "type": "Element",
        }
    )
    primary_index_interval: Optional[AbstractInterval] = field(
        default=None,
        metadata={
            "name": "PrimaryIndexInterval",
            "type": "Element",
        }
    )
    logging_company: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "LoggingCompany",
            "type": "Element",
            "required": True,
        }
    )
    logging_company_code: Optional[int] = field(
        default=None,
        metadata={
            "name": "LoggingCompanyCode",
            "type": "Element",
        }
    )
    channel_kind: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "ChannelKind",
            "type": "Element",
        }
    )
    logging_tool_kind: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "LoggingToolKind",
            "type": "Element",
        }
    )
    logging_tool_class: Optional[Union[LoggingToolType, str]] = field(
        default=None,
        metadata={
            "name": "LoggingToolClass",
            "type": "Element",
            "pattern": r".*:.*",
        }
    )
    derivation: Optional[ChannelDerivation] = field(
        default=None,
        metadata={
            "name": "Derivation",
            "type": "Element",
        }
    )
    logging_method: Optional[LoggingMethod] = field(
        default=None,
        metadata={
            "name": "LoggingMethod",
            "type": "Element",
        }
    )
    nominal_hole_size: Optional[LengthMeasureExt] = field(
        default=None,
        metadata={
            "name": "NominalHoleSize",
            "type": "Element",
        }
    )
    sensor_offset: Optional[LengthMeasureExt] = field(
        default=None,
        metadata={
            "name": "SensorOffset",
            "type": "Element",
        }
    )
    mud_class: Optional[Union[MudType, str]] = field(
        default=None,
        metadata={
            "name": "MudClass",
            "type": "Element",
            "pattern": r".*:.*",
        }
    )
    mud_sub_class: Optional[Union[MudSubType, str]] = field(
        default=None,
        metadata={
            "name": "MudSubClass",
            "type": "Element",
            "pattern": r".*:.*",
        }
    )
    hole_logging_status: Optional[HoleLoggingStatus] = field(
        default=None,
        metadata={
            "name": "HoleLoggingStatus",
            "type": "Element",
        }
    )
    is_continuous: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsContinuous",
            "type": "Element",
        }
    )
    nominal_sampling_interval: Optional[GenericMeasure] = field(
        default=None,
        metadata={
            "name": "NominalSamplingInterval",
            "type": "Element",
        }
    )
    channel_osduintegration: Optional[ChannelOsduintegration] = field(
        default=None,
        metadata={
            "name": "ChannelOSDUIntegration",
            "type": "Element",
        }
    )
    datum: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Datum",
            "type": "Element",
        }
    )
    seismic_reference_elevation: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "SeismicReferenceElevation",
            "type": "Element",
        }
    )
    data: Optional[ChannelData] = field(
        default=None,
        metadata={
            "name": "Data",
            "type": "Element",
        }
    )
    data_source: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "DataSource",
            "type": "Element",
        }
    )
    index: List[ChannelIndex] = field(
        default_factory=list,
        metadata={
            "name": "Index",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    derived_from: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "DerivedFrom",
            "type": "Element",
        }
    )
    wellbore: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Wellbore",
            "type": "Element",
        }
    )
    axis_definition: List[LogChannelAxis] = field(
        default_factory=list,
        metadata={
            "name": "AxisDefinition",
            "type": "Element",
        }
    )
    point_metadata: List[PointMetadata] = field(
        default_factory=list,
        metadata={
            "name": "PointMetadata",
            "type": "Element",
        }
    )
