from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from witsml21.abstract_interval import AbstractInterval
from witsml21.data_object_reference import DataObjectReference
from witsml21.length_uom import LengthUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class MdInterval(AbstractInterval):
    """
    :ivar md_min:
    :ivar md_max:
    :ivar uom:
    :ivar datum: The datum the MD interval is referenced to. Required
        when there is no default MD datum associated with the data
        object this is used in.
    """
    md_min: Optional[float] = field(
        default=None,
        metadata={
            "name": "MdMin",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    md_max: Optional[float] = field(
        default=None,
        metadata={
            "name": "MdMax",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    uom: Optional[Union[LengthUom, str]] = field(
        default=None,
        metadata={
            "name": "Uom",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
            "pattern": r".*:.*",
        }
    )
    datum: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Datum",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
        }
    )
