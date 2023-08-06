from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.abstract_vertical_depth import AbstractVerticalDepth
from witsml21.extension_name_value import ExtensionNameValue
from witsml21.measured_depth import MeasuredDepth
from witsml21.time_measure import TimeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class DrillReportEquipFailureInfo:
    """
    General information about equipment failure that occurred during the drill
    report period.

    :ivar dtim: Date and time that the equipment failed.
    :ivar md: The measured depth of the operation end point where the
        failure happened.
    :ivar tvd: The true vertical depth of the  operation end point where
        failure the failure happened.
    :ivar equip_class: The classification of the equipment that failed.
    :ivar etim_miss_production: The missed production time because of
        the equipment failure.
    :ivar dtim_repair: The date and time at which the production
        equipment was repaired and ready for production.
    :ivar description: A description of the equipment failure.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar uid: Unique identifier for this instance of
        DrillReportEquipFailureInfo.
    """
    dtim: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTim",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    md: Optional[MeasuredDepth] = field(
        default=None,
        metadata={
            "name": "Md",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    tvd: Optional[AbstractVerticalDepth] = field(
        default=None,
        metadata={
            "name": "Tvd",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    equip_class: Optional[str] = field(
        default=None,
        metadata={
            "name": "EquipClass",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    etim_miss_production: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "ETimMissProduction",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    dtim_repair: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimRepair",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 2000,
        }
    )
    extension_name_value: List[ExtensionNameValue] = field(
        default_factory=list,
        metadata={
            "name": "ExtensionNameValue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    uid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 64,
        }
    )
