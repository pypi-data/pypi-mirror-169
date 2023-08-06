from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class ShowLevel(Enum):
    """
    Specifies another qualifier for the show: blooming or streaming.
    """
    BLOOMING = "blooming"
    STREAMING = "streaming"
