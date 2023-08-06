from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class WellboreFluidLocation(Enum):
    """
    Specified the location where cement job fluid can be found.
    """
    ANNULUS = "annulus"
    DEADEND = "deadend"
    IN_PIPE = "in pipe"
    RAT_HOLE = "rat hole"
