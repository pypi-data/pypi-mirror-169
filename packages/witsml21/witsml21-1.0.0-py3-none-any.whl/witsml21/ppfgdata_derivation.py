from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class PpfgdataDerivation(Enum):
    """
    Specifies the source of PPFG data.

    :cvar BASIN_MODEL: Data resulting from general basin modeling.
    :cvar ESTIMATED: Data built as an estimation from another
        datasource.
    :cvar INFERRED: Data inferred from parent data.
    :cvar MEASURED: Data resulting from raw measurement on site.
    :cvar POST_DRILL_INTERPRETATION: Data resulting from a PostDrill
        Interpretation.
    :cvar PRE_DRILL_INTERPRETATION: Data resulting from a PreDrill
        Interpretation.
    :cvar REAL_TIME: Raw dataset resulting from real-time acquisition.
    :cvar TRANSFORMED: Data resulting from a transformation.
    """
    BASIN_MODEL = "basin model"
    ESTIMATED = "estimated"
    INFERRED = "inferred"
    MEASURED = "measured"
    POST_DRILL_INTERPRETATION = "post-drill interpretation"
    PRE_DRILL_INTERPRETATION = "pre-drill interpretation"
    REAL_TIME = "real time"
    TRANSFORMED = "transformed"
