from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class ErrorModelMisalignmentMode(Enum):
    """
    Specifies the various misalignment maths.

    :cvar UNKNOWN:
    :cvar VALUE_1: Alternative 1 as described in SPE 90408.
    :cvar VALUE_2: Alternative 2 as described in SPE 90408.
    :cvar VALUE_3: Alternative 3 as described in SPE 90408.
    """
    UNKNOWN = "unknown"
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
