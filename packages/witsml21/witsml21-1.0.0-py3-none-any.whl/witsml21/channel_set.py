from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional, Union
from witsml21.abstract_active_object import AbstractActiveObject
from witsml21.abstract_interval import AbstractInterval
from witsml21.channel import Channel
from witsml21.channel_data import ChannelData
from witsml21.channel_derivation import ChannelDerivation
from witsml21.channel_index import ChannelIndex
from witsml21.channel_set_osduintegration import ChannelSetOsduintegration
from witsml21.channel_state import ChannelState
from witsml21.data_object_reference import DataObjectReference
from witsml21.generic_measure import GenericMeasure
from witsml21.hole_logging_status import HoleLoggingStatus
from witsml21.length_measure_ext import LengthMeasureExt
from witsml21.logging_method import LoggingMethod
from witsml21.logging_tool_class import LoggingToolType
from witsml21.mud_class import MudType
from witsml21.mud_sub_class import MudSubType
from witsml21.pass_detail import PassDetail

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class ChannelSet(AbstractActiveObject):
    """A grouping of channels with a compatible index, for some purpose.

    Each channel has its own index. A ‘compatible’ index simply means
    that all of the channels are either in time or in depth using a
    common datum.

    :ivar channel_state: Defines where the channel gets its data from,
        e.g., calculated from another source, or from archive, or raw
        real-time, etc.
    :ivar run_number: The nominal run number for the channel. No precise
        meaning is declared for this attribute but it is so commonly
        used that it must be included. The value here should match a bit
        run number for LWD data and a wireline run number for logging
        data.
    :ivar pass_number: The nominal pass number for the channel set. No
        precise meaning is declared for this attribute but it is so
        commonly used that it must be included. The value here should
        match a wireline pass number for logging data. Use PassDetail
        instead if the channel set contains information about several
        passes using PassIndexedDepth.
    :ivar pass_description: The nominal pass description for the pass
        such as Calibration Pass, Main Pass, Repeated Pass. Use
        PassDetail instead if the channel set contains information about
        several passes using PassIndexedDepth.
    :ivar pass_detail: Details about one or more passes when using
        PassIndexedDepth.
    :ivar primary_index_interval: The primary index value range for the
        channel set. This MUST reflect the minimum and maximum primary
        index values for any channels in the channel set. This is
        independent of the direction for the primary index. This MUST be
        specified when there is at least one channel in the channel set
        with data points, and it MUST NOT be specified when there are no
        channels with data points in the channel set. STORE MANAGED.
        This is populated by a store on read. Customer provided values
        are ignored on write
    :ivar logging_company: Pointer to a BusinessAssociate representing
        the logging company.
    :ivar logging_company_code: The RP66 organization code assigned to a
        logging company. The list is available at
        http://www.energistics.org/geosciences/geology-
        standards/rp66-organization-codes
    :ivar logging_tool_kind: An optional value pointing to a
        LoggingToolKind. Energistics provides a list of standard logging
        tool kinds from the Practical Well Logging Standard (PWLS). This
        LoggingToolKind enumeration is in the external
        LoggingToolKindDictionary XML file in the WITSML ancillary
        folder.
    :ivar logging_tool_class: A value categorizing a logging tool. The
        classification system used in WITSML is the one from the PWLS
        group.
    :ivar logging_tool_class_long_name: A long concatenation of the
        tools used for the logging service such as
        GammaRay+NeutronPorosity.
    :ivar derivation: The nominal derivation for channels in the channel
        set. Individual channels may have a different derivation.
    :ivar logging_method: Defines where the log channel gets its data
        from: LWD, MWD, wireline; or whether it is computed, etc
    :ivar nominal_hole_size: The nominal hole size at the time the
        measurement tool was in the hole. The size is "nominal" to
        indicate that this is not the result of a caliper reading or
        other direct measurement of the hole size, but is just a name
        used to refer to the diameter. This is normally the bit size. In
        a case where there are more than one diameter hole being drilled
        at the same time (like where a reamer is behind the bit) this
        diameter is the one which was seen by the sensor which produced
        a particular log channel.
    :ivar mud_class: The nominal class of the drilling fluid at the time
        of logging. Individual channels may have been logged while a
        different drilling fluid was in use.
    :ivar mud_sub_class: The nominal subclass of drilling fluid at the
        time of logging. Individual channels may have been logged while
        a different drilling fluid was in use.
    :ivar hole_logging_status: The nominal status of the hole at the
        time of logging. Individual channels may have been logged while
        the hole was in a different state.
    :ivar nominal_sampling_interval: For regularly sampled channel data,
        this represents the nominal sampling interval. This should only
        be set when it is representative for channels in the channel
        set. Individual channels may have a different nominal sampling
        interval.
    :ivar channel_set_osduintegration: Information about a ChannelSet
        that is relevant for OSDU integration but does not have a
        natural place in a ChannelSet object.
    :ivar index: Defines metadata about the channel set's primary and
        secondary indexes. The first index is the primary index. Any
        additional indexes are secondary indexes. A channel set MUST
        specify this for at least a primary index if it has any channels
        in it. A channel set MAY specify these indexes even if it has no
        channels. All channels within the channel set MUST have indexes
        that are compatible with these indexes.
    :ivar channel:
    :ivar data:
    :ivar wellbore:
    :ivar data_source:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/witsmlv2"

    channel_state: Optional[ChannelState] = field(
        default=None,
        metadata={
            "name": "ChannelState",
            "type": "Element",
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
        }
    )
    logging_company_code: Optional[int] = field(
        default=None,
        metadata={
            "name": "LoggingCompanyCode",
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
    logging_tool_class_long_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "LoggingToolClassLongName",
            "type": "Element",
            "max_length": 256,
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
    nominal_sampling_interval: Optional[GenericMeasure] = field(
        default=None,
        metadata={
            "name": "NominalSamplingInterval",
            "type": "Element",
        }
    )
    channel_set_osduintegration: Optional[ChannelSetOsduintegration] = field(
        default=None,
        metadata={
            "name": "ChannelSetOSDUIntegration",
            "type": "Element",
        }
    )
    index: List[ChannelIndex] = field(
        default_factory=list,
        metadata={
            "name": "Index",
            "type": "Element",
        }
    )
    channel: List[Channel] = field(
        default_factory=list,
        metadata={
            "name": "Channel",
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
    wellbore: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Wellbore",
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
