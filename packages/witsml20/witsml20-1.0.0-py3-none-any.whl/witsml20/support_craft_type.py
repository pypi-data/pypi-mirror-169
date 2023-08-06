from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class SupportCraftType(Enum):
    """
    Specifies the type of support craft.
    """
    BARGE = "barge"
    STANDBY_BOAT = "standby boat"
    HELICOPTER = "helicopter"
    SUPPLY_BOAT = "supply boat"
    TRUCK = "truck"
    CREW_VEHICLE = "crew vehicle"
    TUG_BOAT = "tug boat"
