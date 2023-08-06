from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class ChannelData:
    """
    Contains the bulk data for the log, either as a base64-encoded string or as
    a reference to an external file.

    :ivar data: The data blob in JSON form. This attribute lets you
        embed the bulk data in a single file with the xml, to avoid the
        issues that arise when splitting data across multiple files.
        BUSINESS RULE: Either this element or the FileUri element must
        be present. STORE MANAGED. This is populated by a store on read.
        Customer provided values are ignored on write
    :ivar file_uri: The URI of a file containing the bulk data. If this
        field is non-null, then the data field is ignored. For files
        written to disk, this should normally contain a simple file name
        in relative URI form. For example, if an application writes a
        log file to disk, it might write the xml as abc.xml, and the
        bulk data as abc.avro. In this case, the value of this element
        would be './abc.avro'. BUSINESS RULE: Either this element or the
        Data element must be present.
    """
    data: Optional[str] = field(
        default=None,
        metadata={
            "name": "Data",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    file_uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "FileUri",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
