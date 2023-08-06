from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class SecondMomentOfAreaUom(Enum):
    """
    :cvar CM4: centimetre to the fourth power
    :cvar IN4: inch to the fourth power
    :cvar M4: metre to the fourth power
    """
    CM4 = "cm4"
    IN4 = "in4"
    M4 = "m4"
