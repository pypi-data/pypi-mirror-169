from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class GeologyType(Enum):
    """
    Specifies the values for type of geology.
    """
    AQUIFER = "aquifer"
    RESERVOIR = "reservoir"
