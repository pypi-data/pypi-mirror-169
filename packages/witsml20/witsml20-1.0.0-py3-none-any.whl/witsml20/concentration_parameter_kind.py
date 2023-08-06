from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class ConcentrationParameterKind(Enum):
    """
    Specifies the values for mud log parameters that are measured in units of
    concentration.

    :cvar CUTTINGS_GAS: The cuttings gas concentration averaged over the
        interval.
    """
    CUTTINGS_GAS = "cuttings gas"
