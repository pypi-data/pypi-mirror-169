from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class NameTagTechnology(Enum):
    """
    Specifies the values for the mechanisms for attaching an equipment tag to
    an item.
    """
    INTRINSIC = "intrinsic"
    LABELED = "labeled"
    PAINTED = "painted"
    STAMPED = "stamped"
    TAGGED = "tagged"
    TEMPORARY = "temporary"
