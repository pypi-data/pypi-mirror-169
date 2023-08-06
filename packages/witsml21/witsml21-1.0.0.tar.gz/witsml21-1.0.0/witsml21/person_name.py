from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class PersonName:
    """
    The components of a person's name.

    :ivar prefix: A name prefix. Such as, Dr, Ms, Miss, Mr, etc.
    :ivar first: The person's first name, sometimes called their "given
        name".
    :ivar middle: The person's middle name or initial.
    :ivar last: The person's last or family name.
    :ivar suffix: A name suffix such as Esq, Phd, etc.
    """
    prefix: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prefix",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "max_length": 64,
        }
    )
    first: Optional[str] = field(
        default=None,
        metadata={
            "name": "First",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
            "max_length": 64,
        }
    )
    middle: Optional[str] = field(
        default=None,
        metadata={
            "name": "Middle",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "max_length": 64,
        }
    )
    last: Optional[str] = field(
        default=None,
        metadata={
            "name": "Last",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
            "max_length": 64,
        }
    )
    suffix: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Suffix",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "max_occurs": 9,
            "max_length": 64,
        }
    )
