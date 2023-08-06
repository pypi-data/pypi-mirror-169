from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class ScrType(Enum):
    """
    Specifies the type of slow circulation rate.

    :cvar STRING_ANNULUS:
    :cvar STRING_KILL_LINE:
    :cvar STRING_CHOKE_LINE:
    :cvar UNKNOWN: The value is not known. Avoid using this value. All
        reasonable attempts should be made to determine the appropriate
        value. Use of this value may result in rejection in some
        situations.
    """
    STRING_ANNULUS = "string annulus"
    STRING_KILL_LINE = "string kill line"
    STRING_CHOKE_LINE = "string choke line"
    UNKNOWN = "unknown"
