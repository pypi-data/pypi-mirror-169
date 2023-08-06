from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class ItemState(Enum):
    """
    These values represent the state of a WITSML object.

    :cvar ACTUAL: Actual data measured or entered at the well site.
    :cvar MODEL: Model data used for "what if" calculations.
    :cvar PLAN: A planned object. That is, one which is expected to be
        executed in the future.
    """
    ACTUAL = "actual"
    MODEL = "model"
    PLAN = "plan"
