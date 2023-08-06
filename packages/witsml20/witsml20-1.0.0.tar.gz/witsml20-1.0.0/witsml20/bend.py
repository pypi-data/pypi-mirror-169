from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.custom_data import CustomData
from witsml20.extension_name_value import ExtensionNameValue
from witsml20.length_measure import LengthMeasure
from witsml20.plane_angle_measure import PlaneAngleMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class Bend:
    """
    Tubular Bend Component Schema.

    :ivar angle: Angle of the bend.
    :ivar dist_bend_bot: Distance of the bend from the bottom of the
        component.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar extension_any:
    :ivar uid: Unique identifier for this instance of Bend.
    """
    angle: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "Angle",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    dist_bend_bot: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "DistBendBot",
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
    extension_any: Optional[CustomData] = field(
        default=None,
        metadata={
            "name": "ExtensionAny",
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
