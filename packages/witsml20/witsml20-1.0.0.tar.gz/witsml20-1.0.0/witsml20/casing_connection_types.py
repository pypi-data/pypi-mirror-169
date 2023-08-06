from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class CasingConnectionTypes(Enum):
    """
    Specifies the values for connection type of casing.
    """
    LANDED = "landed"
    SELF_SEALING_THREADED = "self-sealing-threaded"
    WELDED = "welded"
