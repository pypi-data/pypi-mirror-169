from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.address_kind_enum import AddressKindEnum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class GeneralAddress:
    """An general address structure.

    This form is appropriate for most countries.

    :ivar name: The name line of an address. If missing, use the name of
        the business associate.
    :ivar street: A generic term for the middle lines of an address.
        They may be a street address, PO box, suite number, or any lines
        that come between the "name" and "city" lines. This may be
        repeated for up to four, ordered lines.
    :ivar city: The city for the business associate's address.
    :ivar country: The country may be included. Although this is
        optional, it is probably required for most uses.
    :ivar county: The county, if applicable or necessary.
    :ivar postal_code: A postal code, if appropriate for the country. In
        the USA, this would be the five or nine digit zip code.
    :ivar state: State.
    :ivar province: Province.
    :ivar uid: A unique identifier for this data element. It is not
        globally unique (not a uuid) and only need be unique within the
        context of the parent top-level object.
    :ivar kind: The type of address: mailing, physical, or both. See
        AddressKindEnum.
    """
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "max_length": 64,
        }
    )
    street: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Street",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "min_occurs": 1,
            "max_occurs": 4,
            "max_length": 64,
        }
    )
    city: Optional[str] = field(
        default=None,
        metadata={
            "name": "City",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
            "max_length": 64,
        }
    )
    country: Optional[str] = field(
        default=None,
        metadata={
            "name": "Country",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "max_length": 64,
        }
    )
    county: Optional[str] = field(
        default=None,
        metadata={
            "name": "County",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
            "max_length": 64,
        }
    )
    postal_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PostalCode",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "max_length": 64,
        }
    )
    state: Optional[str] = field(
        default=None,
        metadata={
            "name": "State",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
            "max_length": 64,
        }
    )
    province: Optional[str] = field(
        default=None,
        metadata={
            "name": "Province",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
            "max_length": 64,
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
    kind: Optional[AddressKindEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
