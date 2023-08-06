from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class ForceUom(Enum):
    """
    :cvar VALUE_10_K_N: ten kilonewton
    :cvar C_N: centinewton
    :cvar DA_N: dekanewton
    :cvar D_N: decinewton
    :cvar DYNE: dyne
    :cvar EN: exanewton
    :cvar F_N: femtonewton
    :cvar GF: gram-force
    :cvar GN: giganewton
    :cvar H_N: hectonewton
    :cvar KDYNE: kilodyne
    :cvar KGF: thousand gram-force
    :cvar KLBF: thousand pound-force
    :cvar K_N: kilonewton
    :cvar LBF: pound-force
    :cvar MGF: million gram-force
    :cvar M_N: millinewton
    :cvar MN_1: meganewton
    :cvar N: newton
    :cvar N_N: nanonewton
    :cvar OZF: ounce-force
    :cvar PDL: poundal
    :cvar P_N: piconewton
    :cvar TN: teranewton
    :cvar TONF_UK: UK ton-force
    :cvar TONF_US: US ton-force
    :cvar U_N: micronewton
    """
    VALUE_10_K_N = "10 kN"
    C_N = "cN"
    DA_N = "daN"
    D_N = "dN"
    DYNE = "dyne"
    EN = "EN"
    F_N = "fN"
    GF = "gf"
    GN = "GN"
    H_N = "hN"
    KDYNE = "kdyne"
    KGF = "kgf"
    KLBF = "klbf"
    K_N = "kN"
    LBF = "lbf"
    MGF = "Mgf"
    M_N = "mN"
    MN_1 = "MN"
    N = "N"
    N_N = "nN"
    OZF = "ozf"
    PDL = "pdl"
    P_N = "pN"
    TN = "TN"
    TONF_UK = "tonf[UK]"
    TONF_US = "tonf[US]"
    U_N = "uN"
