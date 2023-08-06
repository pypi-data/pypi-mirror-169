from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class BearingType(Enum):
    """
    Specifies the bearing type of a motor.
    """
    OIL_SEAL = "oil seal"
    MUD_LUBE = "mud lube"
    OTHER = "other"
