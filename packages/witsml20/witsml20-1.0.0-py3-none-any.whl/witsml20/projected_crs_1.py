from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from witsml20.abstract_object import AbstractObject
from witsml20.abstract_projected_crs import AbstractProjectedCrs
from witsml20.axis_order2d import AxisOrder2D
from witsml20.length_uom import LengthUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class ProjectedCrs1(AbstractObject):
    """
    This is the Energistics encapsulation of the ProjectedCrs type from GML.
    """
    class Meta:
        name = "ProjectedCrs"

    axis_order: Optional[AxisOrder2D] = field(
        default=None,
        metadata={
            "name": "AxisOrder",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    abstract_projected_crs: Optional[AbstractProjectedCrs] = field(
        default=None,
        metadata={
            "name": "AbstractProjectedCrs",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    uom: Optional[Union[LengthUom, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r".*:.*",
        }
    )
