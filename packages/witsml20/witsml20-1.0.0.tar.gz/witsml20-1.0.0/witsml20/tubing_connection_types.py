from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class TubingConnectionTypes(Enum):
    """
    Specifies the values for the connection types of tubing.
    """
    DOGSCOMPRESSIONFIT_NOTSEALED = "dogscompressionfit-notsealed"
    LANDED = "landed"
    LATCHED = "latched"
    RADIAL = "radial"
    SELFSEALING_THREADED = "selfsealing-threaded"
    SLIPFIT_SEALED = "slipfit-sealed"
    THREADED = "threaded"
