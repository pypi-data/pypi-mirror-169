from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from witsml20.mass_per_mass_uom import MassPerMassUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class MassPerMassMeasureExt:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[Union[MassPerMassUom, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r".*:.*",
        }
    )
