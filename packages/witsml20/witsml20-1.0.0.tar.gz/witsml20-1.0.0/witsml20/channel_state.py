from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class ChannelState(Enum):
    """
    Specifies the source of the data values in the channel, e.g., calculated
    from another source, or from archive, or raw real-time, etc.

    :cvar CALCULATED: Calculated from measurements
    :cvar FINAL: Considered final and not subject to change
    :cvar MEMORY: Sensor data is recorded into downhole memory of a
        tool, rather than transmitting in "real time" to surface.
    :cvar PROCESSED: Results of calculations based on measurements
    :cvar REAL_TIME: Measurements at the actual time.
    """
    CALCULATED = "calculated"
    FINAL = "final"
    MEMORY = "memory"
    PROCESSED = "processed"
    REAL_TIME = "real time"
