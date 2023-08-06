from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.area_per_area_measure import AreaPerAreaMeasure
from witsml20.extension_name_value import ExtensionNameValue
from witsml20.measured_depth_coord import MeasuredDepthCoord
from witsml20.shaker_screen import ShakerScreen
from witsml20.time_measure import TimeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class ShakerOp:
    """
    Operations Shaker Component Schema.

    :ivar shaker: A pointer to the shaker that is characterized by this
        report.
    :ivar md_hole: Hole measured depth at the time of measurement.
    :ivar dtim: Date and time the information is related to.
    :ivar hours_run: Hours run the shaker has run for this operation.
    :ivar pc_screen_covered: Percent of screen covered by cuttings.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar shaker_screen:
    :ivar uid: Unique identifier for this instance of ShakerOp
    """
    shaker: Optional[str] = field(
        default=None,
        metadata={
            "name": "Shaker",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    md_hole: Optional[MeasuredDepthCoord] = field(
        default=None,
        metadata={
            "name": "MdHole",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    dtim: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTim",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    hours_run: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "HoursRun",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pc_screen_covered: Optional[AreaPerAreaMeasure] = field(
        default=None,
        metadata={
            "name": "PcScreenCovered",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    extension_name_value: List[ExtensionNameValue] = field(
        default_factory=list,
        metadata={
            "name": "ExtensionNameValue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    shaker_screen: Optional[ShakerScreen] = field(
        default=None,
        metadata={
            "name": "ShakerScreen",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    uid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 64,
        }
    )
