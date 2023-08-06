from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class CorrectionConsidered(Enum):
    DEPTH = "depth"
    DUAL_INCLINOMETER = "dual inclinometer"
    SAG = "sag"
    COSAG = "cosag"
    AXIAL_MAGNETIC_INTERFERENCE = "axial magnetic interference"
    DRILL_STRING_MAGNETIC_INTERFERENCE = "drill string magnetic interference"
    INTERNATIONAL_GEOMAGNETIC_REFERENCE_FIELD = "international geomagnetic reference field"
    HIGH_RESOLUTION_GEOMAGNETIC_MODEL = "high resolution geomagnetic model"
    IN_FIELD_REFERENCING_1 = "in field referencing 1"
    IN_FIELD_REFERENCING_2 = "in field referencing 2"
    IN_HOLE_REFERENCING = "in hole referencing"
    SINGLE_STATION_ANALYSIS = "single station analysis"
    MULTI_STATION_ANALYSIS = "multi station analysis"
