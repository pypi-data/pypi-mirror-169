from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.abstract_object import AbstractObject
from witsml20.data_object_reference import DataObjectReference
from witsml20.fluid import Fluid
from witsml20.measured_depth_coord import MeasuredDepthCoord
from witsml20.well_vertical_depth_coord import WellVerticalDepthCoord

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class FluidsReport(AbstractObject):
    """
    Used to capture an analysis of the drilling mud.

    :ivar dtim: Date and time the information is related to.
    :ivar md: Along-hole measured depth of measurement from the drill
        datum.
    :ivar tvd: Vertical depth of the measurements.
    :ivar num_report: Fluids report number.
    :ivar fluid:
    :ivar wellbore:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/witsmlv2"

    dtim: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTim",
            "type": "Element",
            "required": True,
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    md: Optional[MeasuredDepthCoord] = field(
        default=None,
        metadata={
            "name": "Md",
            "type": "Element",
            "required": True,
        }
    )
    tvd: Optional[WellVerticalDepthCoord] = field(
        default=None,
        metadata={
            "name": "Tvd",
            "type": "Element",
        }
    )
    num_report: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumReport",
            "type": "Element",
        }
    )
    fluid: List[Fluid] = field(
        default_factory=list,
        metadata={
            "name": "Fluid",
            "type": "Element",
        }
    )
    wellbore: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Wellbore",
            "type": "Element",
            "required": True,
        }
    )
