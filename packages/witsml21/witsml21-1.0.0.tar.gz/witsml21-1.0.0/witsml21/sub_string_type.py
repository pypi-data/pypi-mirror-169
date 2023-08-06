from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class SubStringType(Enum):
    """
    Specifies the values  to further qualify a string type.
    """
    ABANDONED_JUNK_FISH = "abandoned junk/fish"
    CAPILLARY_STRING_INSIDE_TUBING = "capillary string (inside tubing)"
    CAPILLARY_STRING_TUBING_CASING_ANNULUS = "capillary string (tubing/casing annulus)"
    CONDUCTOR_CASING = "conductor casing"
    DRILL_STRING = "drill string"
    FLOWLINE = "flowline"
    GEOLOGICAL_OBJECTS = "geological objects"
    INNER_LINER = "inner liner"
    INTERMEDIATE_CASING = "intermediate casing"
    PRODUCTION_CASING = "production casing"
    PRODUCTION_LINER = "production liner"
    PROTECTIVE_CASING = "protective casing"
    SURFACE_CASING = "surface casing"
    WELLBORE_NOTES = "wellbore notes"
    Y_TOOL_STRING = "y-tool string"
