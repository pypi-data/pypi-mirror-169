from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class FileNameType(Enum):
    """
    Specifies the type of file referenced.

    :cvar FILE_NAME: The file name of the image.
    :cvar PATH_NAME: The path where the file is located.
    :cvar UNIVERSAL_RESOURCE_LOCATOR: A string of characters used to
        identify a resource.
    :cvar OTHER: The value is not known. Avoid using this value. All
        reasonable attempts should be made to determine the appropriate
        value. Use of this value may result in rejection in some
        situations.
    """
    FILE_NAME = "file name"
    PATH_NAME = "path name"
    UNIVERSAL_RESOURCE_LOCATOR = "universal resource locator"
    OTHER = "other"
