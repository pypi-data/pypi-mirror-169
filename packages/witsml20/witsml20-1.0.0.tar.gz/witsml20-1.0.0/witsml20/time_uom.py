from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class TimeUom(Enum):
    """
    :cvar VALUE_1_2_MS: half of millisecond
    :cvar VALUE_100_KA_T: hundred thousand tropical-year
    :cvar A: julian-year
    :cvar A_T: tropical-year
    :cvar CA: hundredth of julian-year
    :cvar CS: centisecond
    :cvar D: day
    :cvar DS: decisecond
    :cvar EA_T: million million million tropical-year
    :cvar FA: femtojulian-year
    :cvar GA_T: thousand million tropical-year
    :cvar H: hour
    :cvar HS: hectosecond
    :cvar KA_T: thousand tropical-year
    :cvar MA_T: million tropical-year
    :cvar MIN: minute
    :cvar MS: millisecond
    :cvar NA: nanojulian-year
    :cvar NS: nanosecond
    :cvar PS: picosecond
    :cvar S: second
    :cvar TA_T: million million tropical-year
    :cvar US: microsecond
    :cvar WK: week
    """
    VALUE_1_2_MS = "1/2 ms"
    VALUE_100_KA_T = "100 ka[t]"
    A = "a"
    A_T = "a[t]"
    CA = "ca"
    CS = "cs"
    D = "d"
    DS = "ds"
    EA_T = "Ea[t]"
    FA = "fa"
    GA_T = "Ga[t]"
    H = "h"
    HS = "hs"
    KA_T = "ka[t]"
    MA_T = "Ma[t]"
    MIN = "min"
    MS = "ms"
    NA = "na"
    NS = "ns"
    PS = "ps"
    S = "s"
    TA_T = "Ta[t]"
    US = "us"
    WK = "wk"
