from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class LinearAccelerationUom(Enum):
    """
    :cvar CM_S2: centimetre per square second
    :cvar FT_S2: foot per second squared
    :cvar GAL: galileo
    :cvar GN: gravity
    :cvar IN_S2: inch per second squared
    :cvar M_S2: metre per second squared
    :cvar M_GAL: milligalileo
    :cvar MGN: thousandth of gravity
    """
    CM_S2 = "cm/s2"
    FT_S2 = "ft/s2"
    GAL = "Gal"
    GN = "gn"
    IN_S2 = "in/s2"
    M_S2 = "m/s2"
    M_GAL = "mGal"
    MGN = "mgn"
