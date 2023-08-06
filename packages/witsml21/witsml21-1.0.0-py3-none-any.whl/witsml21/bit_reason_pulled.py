from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class BitReasonPulled(Enum):
    """
    Specifies the reason for pulling a drill bit from the wellbore, these codes
    were originally defined by the IADC.

    :cvar BHA: Change Bottom Hole Assembly
    :cvar CM: Condition Mud
    :cvar CP: Core Point
    :cvar DMF: Downhole Motor Failure
    :cvar DP: Drill Plug
    :cvar DST: Drill Stem Test
    :cvar DTF: Downhole Tool Failure
    :cvar FM: Formation Change
    :cvar HP: Hole Problems
    :cvar HR: Hours on Bit
    :cvar LOG: Run Logs
    :cvar PP: Pump Pressure
    :cvar PR: Penetration Rate
    :cvar RIG: Rig Repairs
    :cvar TD: Total Depth/Casing Depth
    :cvar TQ: Torque
    :cvar TW: Twist Off
    :cvar WC: Weather Conditions
    """
    BHA = "BHA"
    CM = "CM"
    CP = "CP"
    DMF = "DMF"
    DP = "DP"
    DST = "DST"
    DTF = "DTF"
    FM = "FM"
    HP = "HP"
    HR = "HR"
    LOG = "LOG"
    PP = "PP"
    PR = "PR"
    RIG = "RIG"
    TD = "TD"
    TQ = "TQ"
    TW = "TW"
    WC = "WC"
