from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from witsml20.abstract_object import AbstractObject
from witsml20.abstract_vertical_crs import AbstractVerticalCrs
from witsml20.length_uom import LengthUom
from witsml20.vertical_direction import VerticalDirection

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class VerticalCrs1(AbstractObject):
    class Meta:
        name = "VerticalCrs"

    direction: Optional[VerticalDirection] = field(
        default=None,
        metadata={
            "name": "Direction",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    abstract_vertical_crs: Optional[AbstractVerticalCrs] = field(
        default=None,
        metadata={
            "name": "AbstractVerticalCrs",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    uom: Optional[Union[LengthUom, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r".*:.*",
        }
    )
