from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class ErrorPropagationMode(Enum):
    """
    Specifies the codes for the various propagation modes.

    :cvar B: Bias.
    :cvar R: Random.
    :cvar S: Systematic.
    :cvar W: Well.
    :cvar G: Global.
    """
    B = "B"
    R = "R"
    S = "S"
    W = "W"
    G = "G"
