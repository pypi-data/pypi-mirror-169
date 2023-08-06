from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class MimeType(Enum):
    """
    Specifies the list of mimetypes.

    :cvar IMAGE_TIFF: The image format is Tagged Image File Format.
    :cvar IMAGE_GIF: The image format is Graphic Interchange Format.
    :cvar IMAGE_PNG: The image format is Portable Network Graphics.
    :cvar IMAGE_XML_SVG: The image format is xml with scalable vector
        graphics.
    :cvar OTHER: The value is not known. Avoid using this value. All
        reasonable attempts should be made to determine the appropriate
        value. Use of this value may result in rejection in some
        situations.
    """
    IMAGE_TIFF = "image/tiff"
    IMAGE_GIF = "image/gif"
    IMAGE_PNG = "image/png"
    IMAGE_XML_SVG = "image/xml+svg"
    OTHER = "other"
