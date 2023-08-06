from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class LineStyle(Enum):
    """
    Specifies the style of line used to define the DepthRegTrackCurve.
    """
    DASHED = "dashed"
    SOLID = "solid"
    DOTTED = "dotted"
    SHORT_DASHED = "short dashed"
    LONG_DASHED = "long dashed"
