from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml21.data_object_reference import DataObjectReference
from witsml21.extension_name_value import ExtensionNameValue
from witsml21.name_tag_location import NameTagLocation
from witsml21.name_tag_numbering_scheme import NameTagNumberingScheme
from witsml21.name_tag_technology import NameTagTechnology

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class NameTag:
    """WITSML - Equipment NameTag Schema.

    :ivar name: The physical identification string of the equipment tag.
    :ivar numbering_scheme: The format or encoding specification of the
        equipment tag. The tag may contain different pieces of
        information and knowledge of that information is inherent in the
        specification. The "identification string" is a mandatory part
        of the information in a tag.
    :ivar technology: Identifies the general type of identifier on an
        item.  If multiple identifiers exist on an item, a separate
        description set for each identifier should be created.  For
        example, a joint of casing may have a barcode label on it along
        with a painted-on code and an RFID tag attached or embedded into
        the coupling.  The barcode label may in turn be an RFID-equipped
        label. This particular scenario would require populating five
        nameTags to fully describe and decode all the possible
        identifiers as follows: 'tagged' - RFID tag embedded in the
        coupling, 'label'  - Serial number printed on the label,
        'tagged' - RFID tag embedded into the label, 'label'  - Barcode
        printed on the label, 'painted'- Mill number painted on the pipe
        body.
    :ivar location: An indicator of where the tag is attached to the
        item. This is used to assist the user in finding where an
        identifier is located on an item.  This optional field also
        helps to differentiate where an identifier is located when
        multiple identifiers exist on an item. Most downhole components
        have a box (female thread) and pin (male thread) end as well as
        a pipe body in between the ends. Where multiple identifiers are
        used on an item, it is convenient to have a reference as to
        which end, or somewhere in the middle, an identifier may be
        closer to. Some items may have an identifier on a non-standard
        location, such as on the arm of a hole opener.  'other', by
        exclusion, tells a user to look elsewhere than on the body or
        near the ends of an item.  Most non-downhole tools use either
        'body', 'other' or not specified because the location tends to
        lose value with smaller or non threaded items.
    :ivar installation_date: When the tag was installed in or on the
        item.
    :ivar installation_company: Pointer to a BusinessAssociate
        representing the name of the company that installed the tag.
    :ivar mounting_code: Reference to a manufacturer's or installer's
        installation description, code, or method.
    :ivar comment: A comment or remark about the tag.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar uid: Unique identifier for this instance of NameTag.
    """
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    numbering_scheme: Optional[NameTagNumberingScheme] = field(
        default=None,
        metadata={
            "name": "NumberingScheme",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    technology: Optional[NameTagTechnology] = field(
        default=None,
        metadata={
            "name": "Technology",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    location: Optional[NameTagLocation] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    installation_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "InstallationDate",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    installation_company: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "InstallationCompany",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    mounting_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "MountingCode",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "name": "Comment",
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
