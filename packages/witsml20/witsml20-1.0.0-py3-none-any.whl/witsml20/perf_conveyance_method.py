from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class PerfConveyanceMethod(Enum):
    """
    Information on how perforation is conveyed: slick line, wireline, tubing.
    """
    SLICK_LINE = "slick line"
    TUBING_CONVEYED = "tubing conveyed"
    WIRELINE = "wireline"
