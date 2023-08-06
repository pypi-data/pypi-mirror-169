from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.dipole_moment_uom import DipoleMomentUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class DipoleMomentMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[DipoleMomentUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
