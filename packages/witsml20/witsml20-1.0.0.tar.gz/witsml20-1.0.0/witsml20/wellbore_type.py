from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class WellboreType(Enum):
    """
    Specifies the values for the classification of a wellbore with respect to
    its parent well/wellbore.

    :cvar BYPASS: The original wellbore had to be abandoned before its
        final usage. This wellbore is being drilled as a different
        wellbore, but one which has the same target as the one that was
        abandoned.
    :cvar INITIAL: This is the first wellbore that has been drilled, or
        attempted, in a given well.
    :cvar REDRILL: The wellbore is being redrilled.
    :cvar REENTRY: The wellbore is being reentered after a period of
        abandonment.
    :cvar RESPUD: The wellbore is part of an existing regulatory well.
        The original borehole did not reach the target depth. This
        borehole required the well to be respudded (drilled from a
        different surface position).
    :cvar SIDETRACK: The wellbore is a deviation from a given wellbore
        that produces a different borehole from the others, and whose
        bottomhole differs from any previously existing wellbore
        bottomholes.
    """
    BYPASS = "bypass"
    INITIAL = "initial"
    REDRILL = "redrill"
    REENTRY = "reentry"
    RESPUD = "respud"
    SIDETRACK = "sidetrack"
