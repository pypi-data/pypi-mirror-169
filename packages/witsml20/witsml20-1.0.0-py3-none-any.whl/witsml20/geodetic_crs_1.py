from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.abstract_geodetic_crs import AbstractGeodeticCrs
from witsml20.abstract_object import AbstractObject

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class GeodeticCrs1(AbstractObject):
    class Meta:
        name = "GeodeticCrs"

    abstract_geodetic_crs: Optional[AbstractGeodeticCrs] = field(
        default=None,
        metadata={
            "name": "AbstractGeodeticCrs",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
