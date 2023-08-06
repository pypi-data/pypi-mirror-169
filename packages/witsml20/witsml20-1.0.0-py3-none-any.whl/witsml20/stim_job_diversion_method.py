from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class StimJobDiversionMethod(Enum):
    """
    Specifies the type of diversion used during a stimulation job.
    """
    BALL_SEALER = "ball sealer"
    BANDS = "bands"
    CHEMICAL = "chemical"
    FIBERS = "fibers"
    OTHER = "other"
    PACKER = "packer"
    SOLID_PARTICLE = "solid particle"
    STRADDLE_PACKER = "straddle packer"
