from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class ChannelIndexType(Enum):
    """
    Specifies the type of index used by the channel.

    :cvar MEASURED_DEPTH: Measured depth.
    :cvar TRUE_VERTICAL_DEPTH: True vertical depth.
    :cvar PASS_INDEXED_DEPTH: An index value that includes pass,
        direction, and depth values This can only refer to measured
        depths.
    :cvar DATE_TIME: Date with time.
    :cvar ELAPSED_TIME: Time that has elapsed
    :cvar TEMPERATURE: Temperature.
    :cvar PRESSURE: Pressure.
    """
    MEASURED_DEPTH = "measured depth"
    TRUE_VERTICAL_DEPTH = "true vertical depth"
    PASS_INDEXED_DEPTH = "pass indexed depth"
    DATE_TIME = "date time"
    ELAPSED_TIME = "elapsed time"
    TEMPERATURE = "temperature"
    PRESSURE = "pressure"
