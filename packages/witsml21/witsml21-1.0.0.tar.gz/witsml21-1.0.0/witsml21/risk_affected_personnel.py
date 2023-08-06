from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class RiskAffectedPersonnel(Enum):
    """
    Personnel affected by a risk.

    :cvar CEMENTER:
    :cvar COMPANY_MAN:
    :cvar CONTRACTOR:
    :cvar DIRECTIONAL_DRILLER:
    :cvar DRILLER:
    :cvar DRILLING_ENGINEER:
    :cvar DRILLING_SUPERINTENDENT:
    :cvar DRILLING_TEAM:
    :cvar FACILITY_ENGINEER:
    :cvar FIELD_SERVICE_MANAGER:
    :cvar FOREMAN:
    :cvar GENERAL_SERVICE_SUPERVISOR:
    :cvar GEOLOGIST:
    :cvar MEMBER:
    :cvar MUD_ENGINEER:
    :cvar MUD_LOGGER:
    :cvar MWD_OR_LWD_ENGINEER: measurement while drilling or logging
        while drilling
    :cvar PERFORM_ENGINEER:
    :cvar PETROPHYSICIST:
    :cvar PRODUCTION_ENGINEER:
    :cvar REMOTELY_OPERATED_VEHICLE_ENGINEER:
    :cvar SAFETY_MANAGER:
    :cvar SALES_ENGINEER:
    :cvar SERVICE_SUPERVISOR:
    :cvar TECHNICAL_SUPPORT:
    :cvar TOOL_PUSHER:
    :cvar WIRELINE_ENGINEER:
    """
    CEMENTER = "cementer"
    COMPANY_MAN = "company man"
    CONTRACTOR = "contractor"
    DIRECTIONAL_DRILLER = "directional driller"
    DRILLER = "driller"
    DRILLING_ENGINEER = "drilling engineer"
    DRILLING_SUPERINTENDENT = "drilling superintendent"
    DRILLING_TEAM = "drilling team"
    FACILITY_ENGINEER = "facility engineer"
    FIELD_SERVICE_MANAGER = "field service manager"
    FOREMAN = "foreman"
    GENERAL_SERVICE_SUPERVISOR = "general service supervisor"
    GEOLOGIST = "geologist"
    MEMBER = "member"
    MUD_ENGINEER = "mud engineer"
    MUD_LOGGER = "mud logger"
    MWD_OR_LWD_ENGINEER = "MWD or LWD engineer"
    PERFORM_ENGINEER = "perform engineer"
    PETROPHYSICIST = "petrophysicist"
    PRODUCTION_ENGINEER = "production engineer"
    REMOTELY_OPERATED_VEHICLE_ENGINEER = "remotely operated vehicle engineer"
    SAFETY_MANAGER = "safety manager"
    SALES_ENGINEER = "sales engineer"
    SERVICE_SUPERVISOR = "service supervisor"
    TECHNICAL_SUPPORT = "technical support"
    TOOL_PUSHER = "tool pusher"
    WIRELINE_ENGINEER = "wireline engineer"
