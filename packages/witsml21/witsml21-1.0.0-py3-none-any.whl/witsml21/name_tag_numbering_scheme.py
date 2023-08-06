from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class NameTagNumberingScheme(Enum):
    """
    Specifies the values of the specifications for creating equipment tags.
    """
    ANSI_AIM_BC10 = "ANSI/AIM-BC10"
    ANSI_AIM_BC2 = "ANSI/AIM-BC2"
    ANSI_AIM_BC6 = "ANSI/AIM-BC6"
    EAN_UCC = "EAN.UCC"
    EPC64 = "EPC64"
    EPC96 = "EPC96"
    F2_F = "F2F"
    MFM = "MFM"
    MSRCID = "MSRCID"
    SERIAL_NUMBER = "serial number"
