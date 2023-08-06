from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class ChannelStatus(Enum):
    """
    Specifies the status of the channel (growing object): active, inactive,
    closed.

    :cvar ACTIVE: Actively producing data points.
    :cvar CLOSED: Closed and will never produce new data points.
    :cvar INACTIVE: Currently inactive but may produce data points in
        the future.
    """
    ACTIVE = "active"
    CLOSED = "closed"
    INACTIVE = "inactive"
