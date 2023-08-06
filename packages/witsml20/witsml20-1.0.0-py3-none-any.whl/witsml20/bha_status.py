from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class BhaStatus(Enum):
    """
    Stage of the BHA (plan, progress, final)
    """
    FINAL = "final"
    PROGRESS = "progress"
    PLAN = "plan"
