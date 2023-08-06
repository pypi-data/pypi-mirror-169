from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class PhoneType(Enum):
    """
    Specifies the types phone number (e.g., fax, mobile, etc.)
    """
    FAX = "fax"
    MOBILE = "mobile"
    PAGER = "pager"
    UNKNOWN = "unknown"
    VOICE = "voice"
    VOICE_FAX = "voice/fax"
    VOICEMAIL = "voicemail"
