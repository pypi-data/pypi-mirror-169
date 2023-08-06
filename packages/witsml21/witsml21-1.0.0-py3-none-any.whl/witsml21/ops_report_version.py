from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class OpsReportVersion(Enum):
    """
    Version of the report, e.g., preliminary, normal, final, etc.

    :cvar PRELIMINARY: A report that has not yet been approved by the
        drilling operator. This report is normally issued at the
        beginning of the work day (e.g., 6:00 am).
    :cvar NORMAL: A daily status report that has been approved by the
        drilling operator.
    :cvar FINAL: A report that represents the final definitive status
        for the well. This report is typically issued some period of
        time (e.g., 6 months) after drilling has concluded.
    """
    PRELIMINARY = "preliminary"
    NORMAL = "normal"
    FINAL = "final"
