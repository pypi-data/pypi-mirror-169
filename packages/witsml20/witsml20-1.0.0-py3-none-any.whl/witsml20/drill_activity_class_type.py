from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class DrillActivityTypeType(Enum):
    """
    Activity classifier, e.g., planned, unplanned, downtime.
    """
    PLANNED = "planned"
    UNPLANNED = "unplanned"
    DOWNTIME = "downtime"
