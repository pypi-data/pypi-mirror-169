from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.abstract_object import AbstractObject
from witsml20.channel_status import ChannelStatus
from witsml20.data_object_reference import DataObjectReference
from witsml20.length_measure import LengthMeasure
from witsml20.measured_depth_coord import MeasuredDepthCoord
from witsml20.wellbore_geometry_section import WellboreGeometrySection

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class WellboreGeometry(AbstractObject):
    """Used to capture information about the configuration of the permanently
    installed components in a wellbore.

    This object is uniquely identified within the context of one
    wellbore object.

    :ivar md_base: Measured depth at bottom, at the time this report was
        made.
    :ivar gap_air: Air gap.
    :ivar depth_water_mean: Water depth.
    :ivar growing_status: Describes the growing status of the wellbore
        geometry, whether active, inactive or closed.
    :ivar wellbore_geometry_section:
    :ivar wellbore:
    :ivar bha_run:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/witsmlv2"

    md_base: Optional[MeasuredDepthCoord] = field(
        default=None,
        metadata={
            "name": "MdBase",
            "type": "Element",
        }
    )
    gap_air: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "GapAir",
            "type": "Element",
        }
    )
    depth_water_mean: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "DepthWaterMean",
            "type": "Element",
        }
    )
    growing_status: Optional[ChannelStatus] = field(
        default=None,
        metadata={
            "name": "GrowingStatus",
            "type": "Element",
            "required": True,
        }
    )
    wellbore_geometry_section: List[WellboreGeometrySection] = field(
        default_factory=list,
        metadata={
            "name": "WellboreGeometrySection",
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
    bha_run: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "BhaRun",
            "type": "Element",
        }
    )
