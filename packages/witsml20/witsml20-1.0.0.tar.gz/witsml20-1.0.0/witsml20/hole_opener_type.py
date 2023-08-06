from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class HoleOpenerType(Enum):
    """
    Specifies the types of hole openers.
    """
    UNDER_REAMER = "under-reamer"
    FIXED_BLADE = "fixed blade"
