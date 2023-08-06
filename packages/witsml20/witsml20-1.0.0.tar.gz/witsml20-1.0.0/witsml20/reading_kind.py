from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class ReadingKind(Enum):
    """
    Specifies if the reading was measured or estimated.

    :cvar MEASURED: The reading was measured.
    :cvar ESTIMATED: The reading was estimated.
    :cvar UNKNOWN: The value is not known. Avoid using this value. All
        reasonable attempts should be made to determine the appropriate
        value. Use of this value may result in rejection in some
        situations.
    """
    MEASURED = "measured"
    ESTIMATED = "estimated"
    UNKNOWN = "unknown"
