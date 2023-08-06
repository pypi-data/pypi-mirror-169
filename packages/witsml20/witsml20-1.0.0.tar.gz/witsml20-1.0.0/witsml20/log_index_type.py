from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class LogIndexType(Enum):
    """
    These values represent the type of data used as an index value for a log.

    :cvar DATE_TIME: Log is indexed on date with time.
    :cvar ELAPSED_TIME: Log is indexed on time.
    :cvar LENGTH: Log is indexed on length (not a depth).
    :cvar MEASURED_DEPTH: Log index is a measured depth index.
    :cvar VERTICAL_DEPTH: Log index is a vertical depth depth index .
    :cvar OTHER: Any other index type for a log.
    """
    DATE_TIME = "date time"
    ELAPSED_TIME = "elapsed time"
    LENGTH = "length"
    MEASURED_DEPTH = "measured depth"
    VERTICAL_DEPTH = "vertical depth"
    OTHER = "other"
