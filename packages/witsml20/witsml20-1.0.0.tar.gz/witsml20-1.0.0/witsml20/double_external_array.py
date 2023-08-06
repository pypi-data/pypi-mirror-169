from __future__ import annotations
from dataclasses import dataclass
from witsml20.floating_point_external_array import FloatingPointExternalArray

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class DoubleExternalArray(FloatingPointExternalArray):
    pass
