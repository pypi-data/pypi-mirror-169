from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class AnglePerLengthUom(Enum):
    """
    :cvar VALUE_0_01_DEGA_FT: angular degree per hundred foot
    :cvar VALUE_1_30_DEGA_FT: angular degree per thirty foot
    :cvar VALUE_1_30_DEGA_M: angular degree per thirty metre
    :cvar DEGA_FT: angular degree per foot
    :cvar DEGA_M: angular degree per metre
    :cvar RAD_FT: radian per foot
    :cvar RAD_M: radian per metre
    :cvar REV_FT: revolution per foot
    :cvar REV_M: revolution per metre
    """
    VALUE_0_01_DEGA_FT = "0.01 dega/ft"
    VALUE_1_30_DEGA_FT = "1/30 dega/ft"
    VALUE_1_30_DEGA_M = "1/30 dega/m"
    DEGA_FT = "dega/ft"
    DEGA_M = "dega/m"
    RAD_FT = "rad/ft"
    RAD_M = "rad/m"
    REV_FT = "rev/ft"
    REV_M = "rev/m"
