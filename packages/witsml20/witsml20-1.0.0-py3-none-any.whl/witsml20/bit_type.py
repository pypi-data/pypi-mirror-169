from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class BitType(Enum):
    """
    Specifies the  values that represent the type of drill or core bit.

    :cvar DIAMOND: Diamond bit.
    :cvar DIAMOND_CORE: Diamond core bit.
    :cvar INSERT_ROLLER_CONE: Insert roller cone bit.
    :cvar PDC: Polycrystalline diamond compact fixed-cutter bit.
    :cvar PDC_CORE: Polycrystalline diamond compact core bit.
    :cvar ROLLER_CONE: Milled-tooth roller-cone bit.
    """
    DIAMOND = "diamond"
    DIAMOND_CORE = "diamond core"
    INSERT_ROLLER_CONE = "insert roller cone"
    PDC = "PDC"
    PDC_CORE = "PDC core"
    ROLLER_CONE = "roller cone"
