from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.bit_dull_code import BitDullCode
from witsml21.bit_reason_pulled import BitReasonPulled
from witsml21.bit_type import BitType
from witsml21.cost import Cost
from witsml21.data_object_reference import DataObjectReference
from witsml21.extension_name_value import ExtensionNameValue
from witsml21.iadc_bearing_wear_code import IadcBearingWearCode
from witsml21.iadc_integer_code import IadcIntegerCode
from witsml21.length_measure import LengthMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class BitRecord:
    """Bit Record Component Schema.

    Captures information that describes the bit and problems with the
    bit. Many of the problems are classified using IADC codes that are
    specified as enumerated lists in WITSML.

    :ivar num_bit: Bit number and rerun number, e.g., "4.1" for the
        first rerun of bit 4.
    :ivar dia_bit: Diameter of the drilled hole.
    :ivar dia_pass_thru: Minimum hole or tubing diameter that the bit
        will pass through (for bi-center bits).
    :ivar dia_pilot: Diameter of the pilot bit (for bi-center bits).
    :ivar manufacturer: Pointer to a BusinessAssociate representing the
        manufacturer or supplier of the item.
    :ivar type_bit: Type of bit.
    :ivar code_mfg: The manufacturer's code for the bit.
    :ivar code_iadc: IADC bit code.
    :ivar cond_init_inner: Initial condition of the inner tooth rows
        (inner 2/3 of the bit) (0-8).
    :ivar cond_init_outer: Initial condition of the outer tooth rows
        (outer 1/3 of bit) (0-8).
    :ivar cond_init_dull: Initial dull condition from the IADC bit-wear
        2-character codes.
    :ivar cond_init_location: Initial row and cone numbers for items
        that need location information (e.g., cracked cone, lost cone,
        etc).
    :ivar cond_init_bearing: Initial condition of the bit bearings
        (integer 0-8 or E, F, N or X).
    :ivar cond_init_gauge: Initial condition of the bit gauge in 1/16 of
        an inch. I = in gauge, else the number of 16ths out of gauge.
    :ivar cond_init_other: Other comments on initial bit condition from
        the IADC list (BitDullCode enumerated list).
    :ivar cond_init_reason: Initial reason the bit was pulled from IADC
        codes (BitReasonPulled enumerated list).
    :ivar cond_final_inner: Final condition of the inner tooth rows
        (inner 2/3 of bit) (0-8).
    :ivar cond_final_outer: Final condition of the outer tooth rows
        (outer 1/3 of bit) (0-8).
    :ivar cond_final_dull: Final dull condition from the IADC bit-wear
        2-character codes.
    :ivar cond_final_location: Final conditions for row and cone numbers
        for items that need location information (e.g., cracked cone,
        lost cone, etc).
    :ivar cond_final_bearing: Final condition of the bit bearings
        (integer 0-8 or E, F, N or X).
    :ivar cond_final_gauge: Final condition of the bit gauge in 1/16 of
        a inch. I = in gauge, else number of 16ths out of gauge.
    :ivar cond_final_other: Other final comments on bit condition from
        the IADC list (BitDullCode enumerated list).
    :ivar cond_final_reason: Final reason the bit was pulled from IADC
        codes (BitReasonPulled enumerated list).
    :ivar drive: Bit drive type (motor, rotary table, etc.).
    :ivar bit_class: N = new, U = used.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar cost:
    :ivar uid: Unique identifier for this instance of BitRecord.
    """
    num_bit: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumBit",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    dia_bit: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "DiaBit",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    dia_pass_thru: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "DiaPassThru",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    dia_pilot: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "DiaPilot",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    manufacturer: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Manufacturer",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    type_bit: Optional[BitType] = field(
        default=None,
        metadata={
            "name": "TypeBit",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    code_mfg: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodeMfg",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    code_iadc: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodeIADC",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    cond_init_inner: Optional[IadcIntegerCode] = field(
        default=None,
        metadata={
            "name": "CondInitInner",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    cond_init_outer: Optional[IadcIntegerCode] = field(
        default=None,
        metadata={
            "name": "CondInitOuter",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    cond_init_dull: Optional[BitDullCode] = field(
        default=None,
        metadata={
            "name": "CondInitDull",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    cond_init_location: Optional[str] = field(
        default=None,
        metadata={
            "name": "CondInitLocation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    cond_init_bearing: Optional[IadcBearingWearCode] = field(
        default=None,
        metadata={
            "name": "CondInitBearing",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    cond_init_gauge: Optional[str] = field(
        default=None,
        metadata={
            "name": "CondInitGauge",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    cond_init_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "CondInitOther",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    cond_init_reason: Optional[BitReasonPulled] = field(
        default=None,
        metadata={
            "name": "CondInitReason",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    cond_final_inner: Optional[IadcIntegerCode] = field(
        default=None,
        metadata={
            "name": "CondFinalInner",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    cond_final_outer: Optional[IadcIntegerCode] = field(
        default=None,
        metadata={
            "name": "CondFinalOuter",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    cond_final_dull: Optional[BitDullCode] = field(
        default=None,
        metadata={
            "name": "CondFinalDull",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    cond_final_location: Optional[str] = field(
        default=None,
        metadata={
            "name": "CondFinalLocation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    cond_final_bearing: Optional[IadcBearingWearCode] = field(
        default=None,
        metadata={
            "name": "CondFinalBearing",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    cond_final_gauge: Optional[str] = field(
        default=None,
        metadata={
            "name": "CondFinalGauge",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    cond_final_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "CondFinalOther",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    cond_final_reason: Optional[BitReasonPulled] = field(
        default=None,
        metadata={
            "name": "CondFinalReason",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    drive: Optional[str] = field(
        default=None,
        metadata={
            "name": "Drive",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    bit_class: Optional[str] = field(
        default=None,
        metadata={
            "name": "BitClass",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
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
    cost: Optional[Cost] = field(
        default=None,
        metadata={
            "name": "Cost",
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
