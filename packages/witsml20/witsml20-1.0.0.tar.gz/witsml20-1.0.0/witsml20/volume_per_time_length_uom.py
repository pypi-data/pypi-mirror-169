from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class VolumePerTimeLengthUom(Enum):
    """
    :cvar VALUE_1000_BBL_FT_D: thousand barrel foot per day
    :cvar VALUE_1000_M4_D: thousand (cubic metre per day) metre
    :cvar M4_S: metre to the fourth power per second
    """
    VALUE_1000_BBL_FT_D = "1000 bbl.ft/d"
    VALUE_1000_M4_D = "1000 m4/d"
    M4_S = "m4/s"
