from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.vertical_coordinate_uom import VerticalCoordinateUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class VerticalCoordinateMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[VerticalCoordinateUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
