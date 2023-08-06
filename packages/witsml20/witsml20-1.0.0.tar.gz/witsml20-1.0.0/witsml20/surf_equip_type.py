from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class SurfEquipType(Enum):
    """
    Specifies the type of surface equipment.

    :cvar IADC:
    :cvar CUSTOM:
    :cvar COILED_TUBING:
    :cvar UNKNOWN: The value is not known. Avoid using this value. All
        reasonable attempts should be made to determine the appropriate
        value. Use of this value may result in rejection in some
        situations.
    """
    IADC = "IADC"
    CUSTOM = "custom"
    COILED_TUBING = "coiled tubing"
    UNKNOWN = "unknown"
