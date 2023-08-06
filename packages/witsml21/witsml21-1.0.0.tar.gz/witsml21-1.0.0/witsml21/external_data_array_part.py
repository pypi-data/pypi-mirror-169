from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class ExternalDataArrayPart:
    """
    Pointers to a whole or to a sub-selection of an existing array that is in a
    different file than the Energistics data object.

    :ivar count: For each dimension, the count of elements to select,
        starting from the corresponding StartIndex in the data set
        identified by the attribute PathInExternalFile. If you want to
        select the whole data set identified by PathInExternalFile, then
        put the whole data set dimension count in each dimension.
    :ivar path_in_external_file: A string that is meaningful to the API
        that will store and retrieve data from the external file. - For
        an HDF file, it is the path of the referenced data set in the
        external file. The separator between groups and final data set
        is a slash '/' - For a LAS file, it could be the list of
        mnemonics in the ~A block. - For a SEG-Y file, it could be a
        list of trace headers.
    :ivar start_index: For each dimension, the start index of the
        selection of the data set identified by the attribute
        PathInExternalFile. If you want to select the whole data set
        identified by PathInExternalFile, then put 0 in each dimension.
    :ivar uri: The URI where the DataArrayPart is stored. In an EPC
        context, it should follow the corresponding rel entry URI
        syntax.
    :ivar mime_type: If the resource being pointed to is a file, then
        this is the MIME type of the file.
    """
    count: List[int] = field(
        default_factory=list,
        metadata={
            "name": "Count",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "min_occurs": 1,
            "min_inclusive": 1,
        }
    )
    path_in_external_file: Optional[str] = field(
        default=None,
        metadata={
            "name": "PathInExternalFile",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
            "max_length": 2000,
        }
    )
    start_index: List[int] = field(
        default_factory=list,
        metadata={
            "name": "StartIndex",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "min_occurs": 1,
            "min_inclusive": 0,
        }
    )
    uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "URI",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
            "max_length": 2000,
        }
    )
    mime_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "MimeType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "max_length": 2000,
        }
    )
