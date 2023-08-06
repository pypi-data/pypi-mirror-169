from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class ErrorKind(Enum):
    ALIGNMENT = "alignment"
    AZIMUTH_REFERENCE = "azimuth reference"
    DEPTH = "depth"
    MAGNETIC = "magnetic"
    READING = "reading"
    SENSOR = "sensor"
