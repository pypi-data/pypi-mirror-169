from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class WellTestType(Enum):
    """
    Specifies the type of well test conducted.

    :cvar DRILL_STEM_TEST: Determines the productive capacity, pressure,
        permeability or extent (or a combination of these) of a
        hydrocarbon reservoir, with the drill string still in the hole.
    :cvar PRODUCTION_TEST: Determines the daily rate of oil, gas, and
        water production from a (potential) reservoir.
    """
    DRILL_STEM_TEST = "drill stem test"
    PRODUCTION_TEST = "production test"
