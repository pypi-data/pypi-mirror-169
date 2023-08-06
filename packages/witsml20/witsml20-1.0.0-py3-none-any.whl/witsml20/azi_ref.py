from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class AziRef(Enum):
    """
    Reference to the azimuth of the trajectory.

    :cvar MAGNETIC_NORTH: The north direction as defined by Magnetic
        North Pole at the time of the measurement. The Magnetic North
        Pole is the direction that a magnet points to when freely
        rotating.
    :cvar GRID_NORTH: The north direction is defined by the coordinate
        grid in the projection coordinate system.
    :cvar TRUE_NORTH: The north direction as defined by the true North
        Pole. The true North Pole is an average of the actual measured
        north axis, which is the axis of rotation of the earth.
    """
    MAGNETIC_NORTH = "magnetic north"
    GRID_NORTH = "grid north"
    TRUE_NORTH = "true north"
