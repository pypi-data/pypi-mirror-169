from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class PpfgmainFamily(Enum):
    """The Main Family Type of the PPFG quantity measured, for example 'pore
    pressure'.

    Primarily used for high level data classification.
    """
    COMPACTION_TRENDLINE = "compaction trendline"
    EFFECTIVE_STRESS = "effective stress"
    EFFECTIVE_STRESS_GRADIENT = "effective stress gradient"
    FORMATION_PRESSURE = "formation pressure"
    FORMATION_PRESSURE_GRADIENT = "formation pressure gradient"
    FRACTURE_PRESSURE = "fracture pressure"
    FRACTURE_PRESSURE_GRADIENT = "fracture pressure gradient"
    GEOMECHNANICS = "geomechnanics"
    MARGIN = "margin"
    MPD = "mpd"
    OVERPRESSURE = "overpressure"
    OVERPRESSURE_GRADIENT = "overpressure gradient"
    PORE_PRESSURE = "pore pressure"
    PORE_PRESSURE_GRADIENT = "pore pressure gradient"
    REFERENCE = "reference"
    SEDIMENTATION_RATE = "sedimentation rate"
    STRESS = "stress"
    STRESS_GRADIENT = "stress gradient"
    TEMPERATURE = "temperature"
    TRANSFORM_MODEL_PARAMETER = "transform model parameter"
    WINDOW = "window"
