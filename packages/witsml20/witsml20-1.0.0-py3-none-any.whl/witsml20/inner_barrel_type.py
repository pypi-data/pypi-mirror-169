from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class InnerBarrelType(Enum):
    """
    Core inner barrel type.

    :cvar UNDIFFERENTIATED: A pipe that is located inside a core barrel
        to hold the core sample.
    :cvar ALUMINUM: An inner core barrel made of aluminium.
    :cvar GEL: An inner core barrel that that seals off the core sample
        using gel as the sealing material.
    :cvar FIBERGLASS: An inner core barrel made of glass fiber
        reinforced plastic.
    """
    UNDIFFERENTIATED = "undifferentiated"
    ALUMINUM = "aluminum"
    GEL = "gel"
    FIBERGLASS = "fiberglass"
