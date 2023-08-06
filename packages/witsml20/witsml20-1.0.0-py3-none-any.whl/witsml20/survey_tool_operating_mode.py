from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class SurveyToolOperatingMode(Enum):
    """
    Specifies the codes for the ISCWSA survey tool operating modes.

    :cvar CONTINUOUS_XY:
    :cvar CONTINUOUS_XYZ:
    :cvar CONTINUOUS_Z:
    :cvar UNKNOWN:
    :cvar STATIONARY: Tool is operating in a stationary mode.
    """
    CONTINUOUS_XY = "continuous xy"
    CONTINUOUS_XYZ = "continuous xyz"
    CONTINUOUS_Z = "continuous z"
    UNKNOWN = "unknown"
    STATIONARY = "stationary"
