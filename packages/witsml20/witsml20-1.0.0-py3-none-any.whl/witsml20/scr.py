from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.angular_velocity_measure import AngularVelocityMeasure
from witsml20.extension_name_value import ExtensionNameValue
from witsml20.measured_depth_coord import MeasuredDepthCoord
from witsml20.pressure_measure import PressureMeasure
from witsml20.scr_type import ScrType

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class Scr:
    """
    Operations Slow Circulation Rates (SCR) Component Schema.

    :ivar dtim: Date and time the information is related to.
    :ivar pump: A pointer to the corresponding pump on the rig.
    :ivar type_scr: Type of slow circulation rate.
    :ivar rate_stroke: Pump stroke rate.
    :ivar pres_recorded: Recorded pump pressure for the stroke rate.
    :ivar md_bit: Along hole measured depth of measurement from the
        drill datum.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar uid: Unique identifier for this instance of Scr
    """
    dtim: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTim",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    pump: Optional[int] = field(
        default=None,
        metadata={
            "name": "Pump",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    type_scr: Optional[ScrType] = field(
        default=None,
        metadata={
            "name": "TypeScr",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    rate_stroke: Optional[AngularVelocityMeasure] = field(
        default=None,
        metadata={
            "name": "RateStroke",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    pres_recorded: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "PresRecorded",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    md_bit: Optional[MeasuredDepthCoord] = field(
        default=None,
        metadata={
            "name": "MdBit",
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
    uid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 64,
        }
    )
