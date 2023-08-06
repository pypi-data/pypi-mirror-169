from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class JarAction(Enum):
    """
    Specifies the type of jar action.
    """
    UP = "up"
    DOWN = "down"
    BOTH = "both"
    VIBRATING = "vibrating"
