from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class ScaleType(Enum):
    """
    Specifies the main line scale types.
    """
    LINEAR = "linear"
    LOGARITHMIC = "logarithmic"
