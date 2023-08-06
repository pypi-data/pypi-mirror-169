from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class TubularAssembly(Enum):
    """
    Specifies the type (or purpose) of the tubular assembly.

    :cvar DRILLING:
    :cvar DIRECTIONAL_DRILLING:
    :cvar FISHING:
    :cvar CONDITION_MUD:
    :cvar TUBING_CONVEYED_LOGGING:
    :cvar CEMENTING:
    :cvar CASING:
    :cvar CLEAN_OUT:
    :cvar COMPLETION_OR_TESTING:
    :cvar CORING:
    :cvar HOLE_OPENING_OR_UNDERREAMING:
    :cvar MILLING_OR_DRESSING_OR_CUTTING:
    :cvar WIPER_OR_CHECK_OR_REAMING:
    :cvar UNKNOWN: The value is not known. Avoid using this value. All
        reasonable attempts should be made to determine the appropriate
        value. Use of this value may result in rejection in some
        situations.
    """
    DRILLING = "drilling"
    DIRECTIONAL_DRILLING = "directional drilling"
    FISHING = "fishing"
    CONDITION_MUD = "condition mud"
    TUBING_CONVEYED_LOGGING = "tubing conveyed logging"
    CEMENTING = "cementing"
    CASING = "casing"
    CLEAN_OUT = "clean out"
    COMPLETION_OR_TESTING = "completion or testing"
    CORING = "coring"
    HOLE_OPENING_OR_UNDERREAMING = "hole opening or underreaming"
    MILLING_OR_DRESSING_OR_CUTTING = "milling or dressing or cutting"
    WIPER_OR_CHECK_OR_REAMING = "wiper or check or reaming"
    UNKNOWN = "unknown"
