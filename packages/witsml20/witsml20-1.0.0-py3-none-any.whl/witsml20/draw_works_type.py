from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class DrawWorksType(Enum):
    """
    Specifies the type of draw works.
    """
    MECHANICAL = "mechanical"
    STANDARD_ELECTRIC = "standard electric"
    DIESEL_ELECTRIC = "diesel electric"
    RAM_RIG = "ram rig"
