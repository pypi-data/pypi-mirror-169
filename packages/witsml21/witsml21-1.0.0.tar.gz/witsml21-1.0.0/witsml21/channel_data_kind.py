from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class ChannelDataKind(Enum):
    """
    Specifies the kind of data contained in a channel.

    :cvar BOOLEAN: True or false values.
    :cvar BYTES: Integer data value (nominally a one-byte value). The
        value must conform to the format of the xsd:dateTime data type
        (minInclusive=-128 and maxInclusive=127).
    :cvar DOUBLE: Double-precision floating-point value (nominally an
        8-byte value). The value must conform to the format of the
        xsd:double data type.
    :cvar FLOAT: Single-precision floating-point value (nominally a
        4-byte value). The value must conform to the format of the
        xsd:float data type
    :cvar INT: Integer data value (nominally a 4-byte value). The value
        must conform to the format of the xsd:int data type.
    :cvar LONG: Long integer data value (nominally an 8-byte value). The
        value must conform to the format of the xsd:long data type.
    :cvar STRING: Character string data. The value must conform to the
        format of the xsd:string data type. The maximum length of a
        value is determined by individual servers.
    :cvar MEASURED_DEPTH: Measured depth.
    :cvar TRUE_VERTICAL_DEPTH: True vertical depth.
    :cvar PASS_INDEXED_DEPTH: An index value that includes pass,
        direction, and depth values This can only refer to measured
        depths.
    :cvar DATE_TIME: Date with time.
    :cvar ELAPSED_TIME: Time that has elapsed.
    """
    BOOLEAN = "boolean"
    BYTES = "bytes"
    DOUBLE = "double"
    FLOAT = "float"
    INT = "int"
    LONG = "long"
    STRING = "string"
    MEASURED_DEPTH = "measured depth"
    TRUE_VERTICAL_DEPTH = "true vertical depth"
    PASS_INDEXED_DEPTH = "pass indexed depth"
    DATE_TIME = "date time"
    ELAPSED_TIME = "elapsed time"
