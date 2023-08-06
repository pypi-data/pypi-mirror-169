from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class EventTypeType(Enum):
    """
    Qualifies the type of event: daily report, job, npt, etc.
    """
    DAILY_COST = "daily cost"
    DAILY_REPORT = "daily report"
    FAILURE_DOWNHOLE_EQUIPMENT_ONLY = "failure (downhole equipment only)"
    JOB = "job"
    JOB_PLAN_PHASES = "job plan (phases)"
    MUD_ATTRIBUTES = "mud attributes"
    NPT_LOST_TIME_EVENT = "npt (lost time event)"
    TIME_LOG_TIME_MEASURE = "time log (time measure)"
