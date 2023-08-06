from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class BoreholeType(Enum):
    """
    Specifies the values for the type of borehole.
    """
    CAVERN = "cavern"
    CAVITY = "cavity"
    NORMALBOREHOLE = "normalborehole"
    UNDERREAM = "underream"
