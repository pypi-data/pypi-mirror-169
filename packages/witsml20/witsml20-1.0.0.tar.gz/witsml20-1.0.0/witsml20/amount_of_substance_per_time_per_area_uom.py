from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class AmountOfSubstancePerTimePerAreaUom(Enum):
    """
    :cvar LBMOL_H_FT2: pound-mass-mole per hour square foot
    :cvar LBMOL_S_FT2: pound-mass-mole per second square foot
    :cvar MOL_S_M2: gram-mole per second square metre
    """
    LBMOL_H_FT2 = "lbmol/(h.ft2)"
    LBMOL_S_FT2 = "lbmol/(s.ft2)"
    MOL_S_M2 = "mol/(s.m2)"
