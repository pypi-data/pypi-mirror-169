from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class BackupScaleType(Enum):
    """
    Backup scale types.
    """
    X10 = "x10"
    OFFSCALE_LEFT_RIGHT = "offscale left/right"
    OTHER = "other"
