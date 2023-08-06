from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.abstract_interval import AbstractInterval
from witsml21.data_index_kind import DataIndexKind
from witsml21.data_object_reference import DataObjectReference
from witsml21.depth_reg_calibration_point import DepthRegCalibrationPoint
from witsml21.depth_reg_parameter import DepthRegParameter
from witsml21.depth_reg_rectangle import DepthRegRectangle
from witsml21.depth_reg_track import DepthRegTrack
from witsml21.extension_name_value import ExtensionNameValue
from witsml21.generic_measure import GenericMeasure
from witsml21.length_measure import LengthMeasure
from witsml21.log_section_type import LogSectionType

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class DepthRegLogSection:
    """Defines the description and coordinates of a well log section, the
    curves on the log.

    An important XSDelement to note is log:refNameString; it is a
    reference to the actual log/data (in a WITSML server) that this
    raster image represents; this object does not contain the log data.

    :ivar log_section_sequence_number: Zero-based index in the log
        sections, in order of appearance.
    :ivar log_section_type: Type of log section.
    :ivar log_section_name: Name of a log section;  used to distinguish
        log sections of the same type.
    :ivar log_matrix: Log matrix assumed for porosity computations.
    :ivar scale_numerator: The numerator of the index (depth or time)
        scale of the original log, e. g. "5 in".
    :ivar scale_denominator: The denominator of the index (depth or
        time) scale of the original log, e. g. "100 ft".  '@uom' must be
        consistent with '//indexType'.
    :ivar index_kind: Primary index type. For date-time indexes, any
        specified index values should be defined as a time offset (e.g.,
        in seconds) from the creationDate of the well log.
    :ivar index_uom: Index UOM of the original log.
    :ivar index_datum: Pointer to a reference point representing the
        origin for vertical coordinates on the original log. If this is
        not specified, information about the datum should be specified
        in a comment.
    :ivar index_interval: The range of the index values.
    :ivar vertical_label: Vertical log scale label (e.g., "1 IN/100 F").
    :ivar vertical_ratio: Second term of the vertical scale ratio (e.g.,
        "240" for a 5-inch-per-100-foot log section).
    :ivar comment: Comments about the calibration.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar upper_curve_scale_rect: Boundaries of the upper curve scale
        (or horizontal scale) section for this log section.
    :ivar calibration_point: Generally this associates an X, Y value
        pair with a depth value from the log section.
    :ivar white_space: Defines blank space occurring within a log
        section in an image.
    :ivar lower_curve_scale_rect: Boundaries of the lower curve scale
        (or horizontal scale) section for this log section.
    :ivar log_section_rect: The bounding rectangle of this log section.
    :ivar parameter:
    :ivar track:
    :ivar channel_set:
    :ivar uid: Unique identifier for the log section.
    """
    log_section_sequence_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "LogSectionSequenceNumber",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "min_inclusive": 0,
        }
    )
    log_section_type: Optional[LogSectionType] = field(
        default=None,
        metadata={
            "name": "LogSectionType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    log_section_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "LogSectionName",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    log_matrix: Optional[str] = field(
        default=None,
        metadata={
            "name": "LogMatrix",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    scale_numerator: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "ScaleNumerator",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    scale_denominator: Optional[GenericMeasure] = field(
        default=None,
        metadata={
            "name": "ScaleDenominator",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    index_kind: Optional[DataIndexKind] = field(
        default=None,
        metadata={
            "name": "IndexKind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    index_uom: Optional[str] = field(
        default=None,
        metadata={
            "name": "IndexUom",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    index_datum: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "IndexDatum",
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
            "required": True,
        }
    )
    vertical_label: Optional[str] = field(
        default=None,
        metadata={
            "name": "VerticalLabel",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 2000,
        }
    )
    vertical_ratio: Optional[str] = field(
        default=None,
        metadata={
            "name": "VerticalRatio",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 2000,
        }
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "name": "Comment",
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
    upper_curve_scale_rect: List[DepthRegRectangle] = field(
        default_factory=list,
        metadata={
            "name": "UpperCurveScaleRect",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    calibration_point: List[DepthRegCalibrationPoint] = field(
        default_factory=list,
        metadata={
            "name": "CalibrationPoint",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    white_space: List[DepthRegRectangle] = field(
        default_factory=list,
        metadata={
            "name": "WhiteSpace",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    lower_curve_scale_rect: List[DepthRegRectangle] = field(
        default_factory=list,
        metadata={
            "name": "LowerCurveScaleRect",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    log_section_rect: List[DepthRegRectangle] = field(
        default_factory=list,
        metadata={
            "name": "LogSectionRect",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    parameter: List[DepthRegParameter] = field(
        default_factory=list,
        metadata={
            "name": "Parameter",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    track: List[DepthRegTrack] = field(
        default_factory=list,
        metadata={
            "name": "Track",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    channel_set: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "ChannelSet",
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
