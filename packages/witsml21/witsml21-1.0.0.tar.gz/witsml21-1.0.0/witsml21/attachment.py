from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.abstract_object import AbstractObject
from witsml21.component_reference import ComponentReference
from witsml21.data_object_reference import DataObjectReference
from witsml21.indexable_element import IndexableElement
from witsml21.measured_depth import MeasuredDepth

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class Attachment(AbstractObject):
    """A dedicated object used to attach digital supplemental data (for
    example, a graphic or PDF file) to another data object.

    The attachment is captured as a base 64 binary type.

    :ivar md: The along-hole measured depth within the RepresentedObject
        where the attachment is indexed.
    :ivar sub_object_reference: A reference to a sub-object that is
        defined within the context of the ReferencedObject. This should
        normally refer to recurring components of a growing object. The
        string content is the uid of the sub-object.
    :ivar indexable_element_type: The type of indexable element that the
        attachment is applicable to. If used, it must be one of the
        enumerated values in IndexableElement.
    :ivar indexable_element_index: Index in an indexable element array
        for an attachment.
    :ivar md_bit: The along-hole measured depth of the bit.
    :ivar category: Used to categorize the content when you have
        multiple attachments of the same file type. EXAMPLE: If you have
        attached a JPEG picture of cuttings at a specific depth, you can
        tag it with Category="CuttingsPicture".
    :ivar file_name: A file name associated with the attachment content.
        Note this is NOT a file path and should contain a name only.
    :ivar file_type: The content file type. This field SHOULD be a
        registered mime type as cataloged at
        http://www.iana.org/assignments/media-types/media-types.xhtml.
    :ivar content_uri: A URI pointing to the location of the attached
        content.
    :ivar content: The actual content of the attachment.
    :ivar object_reference:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/commonv2"

    md: Optional[MeasuredDepth] = field(
        default=None,
        metadata={
            "name": "Md",
            "type": "Element",
        }
    )
    sub_object_reference: Optional[ComponentReference] = field(
        default=None,
        metadata={
            "name": "SubObjectReference",
            "type": "Element",
        }
    )
    indexable_element_type: Optional[IndexableElement] = field(
        default=None,
        metadata={
            "name": "IndexableElementType",
            "type": "Element",
        }
    )
    indexable_element_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "IndexableElementIndex",
            "type": "Element",
        }
    )
    md_bit: Optional[MeasuredDepth] = field(
        default=None,
        metadata={
            "name": "MdBit",
            "type": "Element",
        }
    )
    category: Optional[str] = field(
        default=None,
        metadata={
            "name": "Category",
            "type": "Element",
            "max_length": 64,
        }
    )
    file_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "FileName",
            "type": "Element",
            "max_length": 64,
        }
    )
    file_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "FileType",
            "type": "Element",
            "max_length": 64,
        }
    )
    content_uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "ContentUri",
            "type": "Element",
        }
    )
    content: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Content",
            "type": "Element",
            "required": True,
            "format": "base64",
        }
    )
    object_reference: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "ObjectReference",
            "type": "Element",
        }
    )
