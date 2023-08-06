from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class DriveType(Enum):
    """
    Specifies the type of work-string drive (rotary system).

    :cvar COILED_TUBING: Coiled tubing rig
    :cvar ROTARY_KELLY_DRIVE: Kelly drive system
    :cvar TOP_DRIVE: Top Drive
    """
    COILED_TUBING = "coiled tubing"
    ROTARY_KELLY_DRIVE = "rotary kelly drive"
    TOP_DRIVE = "top drive"
