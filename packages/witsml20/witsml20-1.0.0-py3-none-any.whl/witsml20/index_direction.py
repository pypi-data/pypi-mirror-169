from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class IndexDirection(Enum):
    """
    Specifies the direction of the index, whether decreasing or increasing.

    :cvar DECREASING: The sort order of the data row index values.  For
        a "decreasing" direction, the index value of consecutive data
        nodes are descending.
    :cvar INCREASING: The sort order of the data row index values.  For
        an "increasing" direction, the index value of consecutive data
        nodes are ascending.
    """
    DECREASING = "decreasing"
    INCREASING = "increasing"
