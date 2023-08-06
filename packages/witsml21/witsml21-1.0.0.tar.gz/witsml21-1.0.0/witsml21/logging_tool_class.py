from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class LoggingToolType(Enum):
    """
    :cvar AAC: Array Acoustic
    :cvar AC: Acoustic
    :cvar ADEN: Array Density
    :cvar AGR: Array Gamma Ray
    :cvar ARIN: Array Induction Resistivity
    :cvar ARLL: Array Laterolog Resistivity
    :cvar AUX: Auxiliary
    :cvar DEN: Density
    :cvar DIP: Dipmeter
    :cvar DIR: Directional, including gravity, magnetic and gyro tools
    :cvar DYN: Drill String Dynamics, including downhole weight on bit,
        torque, bending and vibration modes
    :cvar FPR: Formation Pressure
    :cvar GR: Gamma Ray
    :cvar HDIA: Hole Diameter
    :cvar INTERP: Petrophysical Interpretation
    :cvar JOINED_GEOPH: Joined Geophysical
    :cvar JOINED_PETRO: Joined Petrophysical
    :cvar NEU: Neutron
    :cvar NMR: Nuclear Magnetic Resonance
    :cvar REMP: Electromagnetic Propagation Resistivity
    :cvar RIN: Induction Resistivity
    :cvar RLL: Laterolog Resistivity
    :cvar RMIC: Micro Resistivity
    :cvar SAMP: Formation Sampling
    :cvar SGR: Spectral Gamma Ray
    :cvar SP: Spontaneous Potential
    :cvar SURF: Surface Sensors
    """
    AAC = "AAC"
    AC = "AC"
    ADEN = "ADEN"
    AGR = "AGR"
    ARIN = "ARIN"
    ARLL = "ARLL"
    AUX = "AUX"
    DEN = "DEN"
    DIP = "DIP"
    DIR = "DIR"
    DYN = "DYN"
    FPR = "FPR"
    GR = "GR"
    HDIA = "HDIA"
    INTERP = "INTERP"
    JOINED_GEOPH = "JOINED_GEOPH"
    JOINED_PETRO = "JOINED_PETRO"
    NEU = "NEU"
    NMR = "NMR"
    REMP = "REMP"
    RIN = "RIN"
    RLL = "RLL"
    RMIC = "RMIC"
    SAMP = "SAMP"
    SGR = "SGR"
    SP = "SP"
    SURF = "SURF"
