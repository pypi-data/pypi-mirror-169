from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class WellControlIncidentType(Enum):
    """
    Specifies the type of a well control incident.

    :cvar SHALLOW_GAS_KICK: Shallow gas is flowing incidentally into a
        well being drilled.
    :cvar WATER_KICK: Water is flowing incidentally into a well being
        drilled.
    :cvar OIL_KICK: Crude oil is flowing incidentally into a well being
        drilled.
    :cvar GAS_KICK: Gas is flowing incidentally into a well being
        drilled.
    """
    SHALLOW_GAS_KICK = "shallow gas kick"
    WATER_KICK = "water kick"
    OIL_KICK = "oil kick"
    GAS_KICK = "gas kick"
