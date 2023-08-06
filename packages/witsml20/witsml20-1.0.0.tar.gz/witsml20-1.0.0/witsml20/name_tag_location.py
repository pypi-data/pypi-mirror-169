from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class NameTagLocation(Enum):
    """
    Specifies the values for the locations where an equipment tag might be
    found.
    """
    BODY = "body"
    BOX = "box"
    OTHER = "other"
    PIN = "pin"
