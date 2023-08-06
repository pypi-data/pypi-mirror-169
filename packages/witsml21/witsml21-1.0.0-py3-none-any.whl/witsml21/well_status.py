from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class WellStatus(Enum):
    """
    These values represent the status of a well or wellbore.

    :cvar ABANDONED: The status of a facility in which drilling,
        completion, and production operations have been permanently
        terminated.
    :cvar ACTIVE: For a well to be active, at least one of its wellbores
        must be active. For a wellbore to be active, at least one of its
        completions must be actively producing or injecting fluids.
    :cvar ACTIVE_INJECTING: Fluids are actively being injected into the
        facility.
    :cvar ACTIVE_PRODUCING: Fluids are actively being produced from the
        facility.
    :cvar COMPLETED: The completion has been installed, but the facility
        is not yet active. This status is appropriate only before the
        initial producing or injecting activity.
    :cvar DRILLING: The status of a well or wellbore in which drilling
        operations have begun, but are not yet completed. The status
        ends when another status becomes appropriate.
    :cvar PARTIALLY_PLUGGED: The wellbore has been plugged from the
        bottom, but only partially to the point where it intersects
        another wellbore.
    :cvar PERMITTED: The facility has received regulatory approvel, but
        drilling has not yet commenced. For a well, it has been spudded.
        For a subsequent wellbore, the whipstock or similar device has
        not yet been set.
    :cvar PLUGGED_AND_ABANDONED: An abandoned well (or wellbore) whose
        wellbores have been plugged in such a manner as to prevent the
        migration of oil, gas, salt water, or other substance from one
        stratum to another. Generally the criteria for this status is
        controlled by regulatory authorities.
    :cvar PROPOSED: The status of a well or wellbore from conception to
        either regulatory approval or commencement of drilling.
    :cvar SOLD: The facility has been sold, so it is no longer
        appropriate to keep a close internal status value. Status values
        may be added at later times without changing the sold status.
    :cvar SUSPENDED: Production or injection has been temporarily
        suspended in a manner that will allow immediate resumption of
        activities.
    :cvar TEMPORARILY_ABANDONED: Production or injection has been
        temporarily suspended in a manner that will not allow immediate
        resumption of activities.
    :cvar TESTING: The facility operations are suspended while tests are
        being conducted to determine formation and/or reservoir
        properties. For example, a drillstem test. This status also
        includes extended testing.
    :cvar TIGHT: Information about the status of the well is
        confidential. This is more explicit than unknown, since it gives
        the reason that the status value is unknown.
    :cvar WORKING_OVER: Maintenance or data acquisition on a well during
        the production phase. This includes any relevant job which can
        be done while the well is shut in. This includes many jobs that
        occur when a well is re-entered.
    :cvar UNKNOWN: The value is not known. This value should not be used
        in normal situations. All reasonable attempts should be made to
        determine the appropriate value. Use of this value may result in
        rejection in some situations.
    """
    ABANDONED = "abandoned"
    ACTIVE = "active"
    ACTIVE_INJECTING = "active -- injecting"
    ACTIVE_PRODUCING = "active -- producing"
    COMPLETED = "completed"
    DRILLING = "drilling"
    PARTIALLY_PLUGGED = "partially plugged"
    PERMITTED = "permitted"
    PLUGGED_AND_ABANDONED = "plugged and abandoned"
    PROPOSED = "proposed"
    SOLD = "sold"
    SUSPENDED = "suspended"
    TEMPORARILY_ABANDONED = "temporarily abandoned"
    TESTING = "testing"
    TIGHT = "tight"
    WORKING_OVER = "working over"
    UNKNOWN = "unknown"
