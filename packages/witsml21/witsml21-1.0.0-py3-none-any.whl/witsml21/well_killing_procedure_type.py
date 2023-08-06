from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class WellKillingProcedureType(Enum):
    """Specifies the type of procedure used to stop (kill) the flow of
    formation fluids into a well.

    A well-killing procedure may be planned or unplanned. The particular
    situation determines what type of procedure is used.

    :cvar DRILLERS_METHOD: Prescribes circulating the kick fluids out of
        the well and then circulating a higher density kill mud into the
        well through a kill line with an adjustable choke.
    :cvar WAIT_AND_WEIGHT: Prescribes circulating heavier kill mud while
        a constant downhole pressure is maintained by pressure relief
        through a choke.
    :cvar BULLHEADING: Prescribes pumping kill-weight fluid down the
        tubing and forcing the wellbore fluids back into the formation
        through the perforations.
    :cvar LUBRICATE_AND_BLEED: Prescribes this process: 1) Pump a volume
        of killing fluid corresponding to half the volume of the well
        tubing into the well. 2) Observe the well for 30 to 60 minutes
        and wait for the tubing head pressure to drop. 3) Pump
        additional killing fluid into the well. 4) When the wellhead
        pressure drops below 200 psi above observed tubing head
        pressure, bleed off gas from the tubing at high rate.
    :cvar FORWARD_CIRCULATION: Prescribes circulating drilling fluid
        down the tubing, through a circulation device (or out the end of
        a workstring/coiled tubing) and up the annulus.
    :cvar REVERSE_CIRCULATION: Prescribes circulating a drilling fluid
        down the completion annulus, workstring annulus, or pipe annulus
        and taking returns up the tubing, workstring, or pipe.
    """
    DRILLERS_METHOD = "drillers method"
    WAIT_AND_WEIGHT = "wait and weight"
    BULLHEADING = "bullheading"
    LUBRICATE_AND_BLEED = "lubricate and bleed"
    FORWARD_CIRCULATION = "forward circulation"
    REVERSE_CIRCULATION = "reverse circulation"
