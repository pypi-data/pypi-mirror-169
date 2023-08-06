from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional, Union
from witsml21.abstract_active_object import AbstractActiveObject
from witsml21.abstract_interval import AbstractInterval
from witsml21.channel_derivation import ChannelDerivation
from witsml21.channel_set import ChannelSet
from witsml21.channel_state import ChannelState
from witsml21.data_object_reference import DataObjectReference
from witsml21.date_time_interval import DateTimeInterval
from witsml21.generic_measure import GenericMeasure
from witsml21.hole_logging_status import HoleLoggingStatus
from witsml21.length_measure_ext import LengthMeasureExt
from witsml21.log_osduintegration import LogOsduintegration
from witsml21.logging_method import LoggingMethod
from witsml21.logging_tool_class import LoggingToolType
from witsml21.mud_class import MudType
from witsml21.mud_sub_class import MudSubType
from witsml21.pass_detail import PassDetail

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class Log(AbstractActiveObject):
    """Primarily a container for one or more channel sets (ChannelSet).

    In WITSML v2.+, most of the log information is now at the channel
    set level. The concept of multiple channel sets in a single log is
    significant change from WITSML v1.4.1.1, where each log represented
    exactly one group of curves and their data. For more information
    about log organization and how it works, see the WITSML Technical
    Usage Guide.

    :ivar channel_state: Defines where the channel gets its data from,
        e.g., calculated from another source, or from archive, or raw
        real-time, etc.
    :ivar run_number: Should be a nominal value intended as a guide that
        applies to all or most ChannelSets and Channels in the Log.
        Should NOT be populated if the value does not apply for the
        majority of the ChannelSets and Channels. The value here should
        match a bit run number for LWD data and a wireline run number
        for logging data.
    :ivar pass_number: Should be a nominal value intended as a guide
        that applies to all or most ChannelSets and Channels in the Log.
        Should NOT be populated if the value does not apply for the
        majority of the ChannelSets and Channels. Use PassDetail instead
        if the log contains information about several passes using
        PassIndexedDepth.
    :ivar pass_description: The nominal pass description for the pass
        such as Calibration Pass, Main Pass, Repeated Pass. Use
        PassDetail instead if the log contains information about several
        passes using PassIndexedDepth.
    :ivar pass_detail: Details about one or more passes when using
        PassIndexedDepth.
    :ivar primary_index_interval: If all channel sets within the log
        have a compatible primary index, this is the primary index value
        range for the channel sets in the log. When specified, this MUST
        reflect the minimum and maximum primary index values for any
        channel sets in the log. This is independent of the direction
        for the primary index. This MAY be specified if all channel sets
        in the log have a compatible primary index AND at least one
        channel set has at least one channel with data points. This MUST
        NOT be specified if any channel sets in the log have
        incompatible primary indexes OR no channel sets in the log have
        channels with any data points. STORE MANAGED. This is populated
        by a store on read. Customer provided values are ignored on
        write
    :ivar logging_company: Pointer to a BusinessAssociate representing
        the logging company. Should be a nominal value intended as a
        guide that applies to all or most ChannelSets and Channels in
        the Log. Should NOT be populated if the value does not apply for
        the majority of the ChannelSets and Channels.
    :ivar logging_company_code: The RP66 organization code assigned to a
        logging company. The list is available at
        http://www.energistics.org/geosciences/geology-
        standards/rp66-organization-codes Should be a nominal value
        intended as a guide that applies to all or most ChannelSets and
        Channels in the Log. Should NOT be populated if the value does
        not apply for the majority of the ChannelSets and Channels.
    :ivar logging_tool_kind: An optional value pointing to a
        LoggingToolKind. Energistics provides a list of standard logging
        tool kinds from the Practical Well Logging Standard (PWLS). This
        LoggingToolKind enumeration is in the external
        LoggingToolKindDictionary XML file in the WITSML ancillary
        folder. Should be a nominal value intended as a guide that
        applies to all or most ChannelSets and Channels in the Log.
        Should NOT be populated if the value does not apply for the
        majority of the ChannelSets and Channels.
    :ivar logging_tool_class: A value categorizing a logging tool. The
        classification system used in WITSML is the one from the PWLS
        group. Should be a nominal value intended as a guide that
        applies to all or most ChannelSets and Channels in the Log.
        Should NOT be populated if the value does not apply for the
        majority of the ChannelSets and Channels.
    :ivar logging_tool_class_long_name: A long concatenation of the
        tools used for the logging service such as
        GammaRay+NeutronPorosity.
    :ivar logging_service_period: The time interval during which the
        logging service was performed that acquired the data in the
        channel set.
    :ivar derivation: The nominal derivation for channels in the log.
        Individual channels and channel sets may have different
        derivations. Should be a nominal value intended as a guide that
        applies to all or most ChannelSets and Channels in the Log.
        Should NOT be populated if the value does not apply for the
        majority of the ChannelSets and Channels.
    :ivar logging_method: Defines where the log channel gets its data
        from: LWD, MWD, wireline; or whether it is computed, etc. Should
        be a nominal value intended as a guide that applies to all or
        most ChannelSets and Channels in the Log. Should NOT be
        populated if the value does not apply for the majority of the
        ChannelSets and Channels.
    :ivar nominal_hole_size: The nominal hole size at the time the
        measurement tool was in the hole. The size is "nominal" to
        indicate that this is not the result of a caliper reading or
        other direct measurement of the hole size, but is just a name
        used to refer to the diameter. This is normally the bit size. In
        a case where there are more than one diameter hole being drilled
        at the same time (like where a reamer is behind the bit) this
        diameter is the one which was seen by the sensor which produced
        a particular log channel. Should be a nominal value intended as
        a guide that applies to all or most ChannelSets and Channels in
        the Log. Should NOT be populated if the value does not apply for
        the majority of the ChannelSets and Channels.
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
        be set when it is representative for channels in the log.
        Individual channels may have a different nominal sampling
        interval.
    :ivar log_osduintegration: Information about a Log that is relevant
        for OSDU integration but does not have a natural place in a Log
        object.
    :ivar channel_set:
    :ivar wellbore: The wellbore the log is associated with. This
        element MUST be populated if ALL channel sets and channels in
        the log refer to the same wellbore. It MAY be omitted if they do
        not.
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
    logging_service_period: Optional[DateTimeInterval] = field(
        default=None,
        metadata={
            "name": "LoggingServicePeriod",
            "type": "Element",
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
    log_osduintegration: Optional[LogOsduintegration] = field(
        default=None,
        metadata={
            "name": "LogOSDUIntegration",
            "type": "Element",
        }
    )
    channel_set: List[ChannelSet] = field(
        default_factory=list,
        metadata={
            "name": "ChannelSet",
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
