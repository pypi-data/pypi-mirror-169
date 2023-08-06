from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class IadcIntegerCode(Enum):
    """
    Specifies the IADC integer codes for the inner or outer tooth rows.
    """
    VALUE_0 = "0"
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"
    VALUE_5 = "5"
    VALUE_6 = "6"
    VALUE_7 = "7"
    VALUE_8 = "8"
