from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class PressureParameterKind(Enum):
    """
    Specifies values for mud log parameters that are measured in units of
    pressure.
    """
    DIRECT_FRACTURE_PRESSURE_MEASUREMENT = "direct fracture pressure measurement"
    PORE_PRESSURE_ESTIMATE_WHILE_DRILLING = "pore pressure estimate while drilling"
