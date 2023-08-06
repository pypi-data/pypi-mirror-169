from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class BopType(Enum):
    """
    Specifies the type of blowout preventer.
    """
    ANNULAR_PREVENTER = "annular preventer"
    SHEAR_RAM = "shear ram"
    BLIND_RAM = "blind ram"
    PIPE_RAM = "pipe ram"
    DRILLING_SPOOL = "drilling spool"
    FLEXIBLE_JOINT = "flexible joint"
    CONNECTOR = "connector"
