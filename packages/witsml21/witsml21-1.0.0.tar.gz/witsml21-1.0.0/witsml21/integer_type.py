from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class IntegerType(Enum):
    ARRAY_OF_INT8 = "arrayOfInt8"
    ARRAY_OF_UINT8 = "arrayOfUInt8"
    ARRAY_OF_INT16_LE = "arrayOfInt16LE"
    ARRAY_OF_INT32_LE = "arrayOfInt32LE"
    ARRAY_OF_INT64_LE = "arrayOfInt64LE"
    ARRAY_OF_UINT16_LE = "arrayOfUInt16LE"
    ARRAY_OF_UINT32_LE = "arrayOfUInt32LE"
    ARRAY_OF_UINT64_LE = "arrayOfUInt64LE"
    ARRAY_OF_INT16_BE = "arrayOfInt16BE"
    ARRAY_OF_INT32_BE = "arrayOfInt32BE"
    ARRAY_OF_INT64_BE = "arrayOfInt64BE"
    ARRAY_OF_UINT16_BE = "arrayOfUInt16BE"
    ARRAY_OF_UINT32_BE = "arrayOfUInt32BE"
    ARRAY_OF_UINT64_BE = "arrayOfUInt64BE"
