from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class VolumePerTimePerAreaUom(Enum):
    """
    :cvar FT3_MIN_FT2: cubic foot per minute square foot
    :cvar FT3_S_FT2: cubic foot per second square foot
    :cvar GAL_UK_H_FT2: UK gallon per hour square foot
    :cvar GAL_UK_H_IN2: UK gallon per hour square inch
    :cvar GAL_UK_MIN_FT2: UK gallon per minute square foot
    :cvar GAL_US_H_FT2: US gallon per hour square foot
    :cvar GAL_US_H_IN2: US gallon per hour square inch
    :cvar GAL_US_MIN_FT2: US gallon per minute square foot
    :cvar M3_S_M2: cubic metre per second square metre
    """
    FT3_MIN_FT2 = "ft3/(min.ft2)"
    FT3_S_FT2 = "ft3/(s.ft2)"
    GAL_UK_H_FT2 = "gal[UK]/(h.ft2)"
    GAL_UK_H_IN2 = "gal[UK]/(h.in2)"
    GAL_UK_MIN_FT2 = "gal[UK]/(min.ft2)"
    GAL_US_H_FT2 = "gal[US]/(h.ft2)"
    GAL_US_H_IN2 = "gal[US]/(h.in2)"
    GAL_US_MIN_FT2 = "gal[US]/(min.ft2)"
    M3_S_M2 = "m3/(s.m2)"
