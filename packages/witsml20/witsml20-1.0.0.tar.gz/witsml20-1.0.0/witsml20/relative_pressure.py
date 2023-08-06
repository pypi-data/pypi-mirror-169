from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.abstract_pressure_value import AbstractPressureValue
from witsml20.pressure_measure import PressureMeasure
from witsml20.reference_pressure import ReferencePressure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class RelativePressure(AbstractPressureValue):
    relative_pressure: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "RelativePressure",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    reference_pressure: Optional[ReferencePressure] = field(
        default=None,
        metadata={
            "name": "ReferencePressure",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
