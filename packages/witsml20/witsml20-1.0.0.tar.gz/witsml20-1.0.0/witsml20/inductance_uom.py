from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class InductanceUom(Enum):
    """
    :cvar C_H: centihenry
    :cvar D_H: decihenry
    :cvar EH: exahenry
    :cvar F_H: femtohenry
    :cvar GH: gigahenry
    :cvar H: henry
    :cvar K_H: kilohenry
    :cvar MH: megahenry
    :cvar M_H_1: millihenry
    :cvar N_H: nanohenry
    :cvar TH: terahenry
    :cvar U_H: microhenry
    """
    C_H = "cH"
    D_H = "dH"
    EH = "EH"
    F_H = "fH"
    GH = "GH"
    H = "H"
    K_H = "kH"
    MH = "MH"
    M_H_1 = "mH"
    N_H = "nH"
    TH = "TH"
    U_H = "uH"
