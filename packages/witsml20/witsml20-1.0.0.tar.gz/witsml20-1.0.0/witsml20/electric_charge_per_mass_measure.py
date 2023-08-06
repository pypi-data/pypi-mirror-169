from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.electric_charge_per_mass_uom import ElectricChargePerMassUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class ElectricChargePerMassMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[ElectricChargePerMassUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
