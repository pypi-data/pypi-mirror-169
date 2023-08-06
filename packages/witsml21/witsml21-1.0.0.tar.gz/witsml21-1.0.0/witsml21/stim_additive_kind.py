from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class StimAdditiveKind(Enum):
    """
    Specifies the type of stimulation additive added to the fluid used in the
    stim job.
    """
    ACID = "acid"
    ACTIVATOR = "activator"
    BIOCIDE = "biocide"
    BREAKER = "breaker"
    BREAKER_AID = "breaker aid"
    BUFFER = "buffer"
    CLAY_STABILIZER = "clay stabilizer"
    CORROSION_INHIBITOR = "corrosion inhibitor"
    CORROSION_INHIBITOR_AID = "corrosion inhibitor aid"
    CROSSLINKER = "crosslinker"
    DELAYING_AGENT = "delaying agent"
    FIBERS = "fibers"
    FLUID_LOSS_ADDITIVE = "fluid loss additive"
    FOAMER = "foamer"
    FRICTION_REDUCER = "friction reducer"
    GELLING_AGENT = "gelling agent"
    IRON_CONTROL_ADDITIVE = "iron control additive"
    MUTUAL_SOLVENT = "mutual solvent"
    SALT = "salt"
    STABILIZER = "stabilizer"
    SURFACTANT = "surfactant"
