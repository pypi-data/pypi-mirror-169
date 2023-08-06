from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from witsml20.moment_of_inertia_uom import MomentOfInertiaUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class MomentOfInertiaMeasureExt:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[Union[MomentOfInertiaUom, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r".*:.*",
        }
    )
