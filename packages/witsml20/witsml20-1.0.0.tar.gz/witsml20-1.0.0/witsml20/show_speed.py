from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class ShowSpeed(Enum):
    """Specifies an indication of both the solubility of the oil and the
    permeability of the show.

    The speed can vary from instantaneous to very slow.
    """
    SLOW = "slow"
    MODERATELY_FAST = "moderately fast"
    FAST = "fast"
    INSTANTANEOUS = "instantaneous"
    NONE = "none"
