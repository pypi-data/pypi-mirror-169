from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class DeflectionMethod(Enum):
    """
    Specifies the method used to direct the deviation of the trajectory in
    directional drilling.

    :cvar HYBRID: Rotary steerable system that changes the trajectory of
        a wellbore using both point-the-bit and push-the-bit methods.
    :cvar POINT_BIT: Rotary steerable system that changes the trajectory
        of a wellbore by tilting the bit to point it in the desired
        direction.
    :cvar PUSH_BIT: Rotary steerable system that changes the trajectory
        of a wellbore by inducing a side force to push the bit in the
        desired direction.
    """
    HYBRID = "hybrid"
    POINT_BIT = "point bit"
    PUSH_BIT = "push bit"
