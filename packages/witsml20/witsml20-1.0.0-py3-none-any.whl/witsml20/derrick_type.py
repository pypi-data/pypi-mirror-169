from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class DerrickType(Enum):
    """
    Specifies the type of drilling derrick.

    :cvar DOUBLE: 2-stand capacity derrick.
    :cvar QUADRUPLE: 4-stand capacity derrick.
    :cvar SLANT: Slant derrick.
    :cvar TRIPLE: 3-stand capacity derrick.
    """
    DOUBLE = "double"
    QUADRUPLE = "quadruple"
    SLANT = "slant"
    TRIPLE = "triple"
