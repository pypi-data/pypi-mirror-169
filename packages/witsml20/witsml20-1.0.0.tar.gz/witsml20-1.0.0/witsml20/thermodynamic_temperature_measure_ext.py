from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from witsml20.thermodynamic_temperature_uom import ThermodynamicTemperatureUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class ThermodynamicTemperatureMeasureExt:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[Union[ThermodynamicTemperatureUom, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r".*:.*",
        }
    )
