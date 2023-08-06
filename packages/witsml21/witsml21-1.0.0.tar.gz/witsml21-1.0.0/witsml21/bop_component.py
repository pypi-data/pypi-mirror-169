from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.bop_type import BopType
from witsml21.extension_name_value import ExtensionNameValue
from witsml21.length_measure import LengthMeasure
from witsml21.pressure_measure import PressureMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class BopComponent:
    """
    Blowout Preventer Component Schema.

    :ivar type_bop_comp: Type of ram or preventer.
    :ivar desc_comp: Description of the component.
    :ivar id_pass_thru: Inner diameter that tubulars can pass through.
    :ivar pres_work: Working rating pressure of the component.
    :ivar dia_close_mn: Minimum diameter of the component it will seal.
    :ivar dia_close_mx: Maximum diameter of the component it will seal.
    :ivar nomenclature: Arrangement nomenclature for the blowout
        preventer stack (e.g., S, R, A).
    :ivar is_variable: Is ram bore variable or single size? Defaults to
        false. Values are "true" (or "1") and "false" (or "0").
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar uid: Unique identifier for this instance of BopComponent
    """
    type_bop_comp: Optional[BopType] = field(
        default=None,
        metadata={
            "name": "TypeBopComp",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    desc_comp: Optional[str] = field(
        default=None,
        metadata={
            "name": "DescComp",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    id_pass_thru: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "IdPassThru",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pres_work: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "PresWork",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    dia_close_mn: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "DiaCloseMn",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    dia_close_mx: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "DiaCloseMx",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    nomenclature: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nomenclature",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    is_variable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsVariable",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
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
