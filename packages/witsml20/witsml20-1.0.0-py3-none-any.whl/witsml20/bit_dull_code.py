from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class BitDullCode(Enum):
    """
    Specifies the reason a drill bit was declared inoperable; these codes were
    originally defined by the IADC.

    :cvar BC: Broken Cone
    :cvar BT: Broken teeth/cutters
    :cvar BU: Balled Up
    :cvar CC: Cracked Cone
    :cvar CD: Cone Dragged
    :cvar CI: Cone Interference
    :cvar CR: Cored
    :cvar CT: Chipped Teeth
    :cvar ER: Erosion
    :cvar FC: Flat Crested Wear
    :cvar HC: Heat Checking
    :cvar JD: Junk Damage
    :cvar LC: Lost Cone
    :cvar LN: Lost Nozzle
    :cvar LT: Lost Teeth/Cutters
    :cvar NO: No Dull/No Other Wear
    :cvar OC: Off-Center Wear
    :cvar PB: Pinched Bit
    :cvar PN: Plugged Nozzle
    :cvar RG: Rounded Gauge
    :cvar RO: Ring Out
    :cvar SD: Shirttail Damage
    :cvar SS: Self-Sharpening Wear
    :cvar TR: Tracking
    :cvar WO: WashOut on Bit
    :cvar WT: Worn Teeth/Cutters
    """
    BC = "BC"
    BT = "BT"
    BU = "BU"
    CC = "CC"
    CD = "CD"
    CI = "CI"
    CR = "CR"
    CT = "CT"
    ER = "ER"
    FC = "FC"
    HC = "HC"
    JD = "JD"
    LC = "LC"
    LN = "LN"
    LT = "LT"
    NO = "NO"
    OC = "OC"
    PB = "PB"
    PN = "PN"
    RG = "RG"
    RO = "RO"
    SD = "SD"
    SS = "SS"
    TR = "TR"
    WO = "WO"
    WT = "WT"
