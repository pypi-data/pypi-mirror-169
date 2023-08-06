from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.extension_name_value import ExtensionNameValue
from witsml20.length_measure import LengthMeasure
from witsml20.md_interval import MdInterval
from witsml20.plane_angle_measure import PlaneAngleMeasure
from witsml20.reciprocal_length_measure import ReciprocalLengthMeasure
from witsml20.tvd_interval import TvdInterval

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class PerfHole:
    """
    Information on the perforated hole.

    :ivar md_interval: Measured depth interval for the perforation hole.
    :ivar tvd_interval: The true vertical depth that describes the hole.
    :ivar hole_diameter: The diameter of the hole.
    :ivar hole_angle: The angle of the holes.
    :ivar hole_pattern: The pattern of the holes.
    :ivar remarks: Remarks and comments about this perforated hole.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar hole_density: The density of the holes.
    :ivar hole_count: The number of holes.
    :ivar uid: Unique identifier for this instance of PerfHole.
    """
    md_interval: Optional[MdInterval] = field(
        default=None,
        metadata={
            "name": "MdInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    tvd_interval: Optional[TvdInterval] = field(
        default=None,
        metadata={
            "name": "TvdInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    hole_diameter: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "HoleDiameter",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    hole_angle: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "HoleAngle",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    hole_pattern: Optional[str] = field(
        default=None,
        metadata={
            "name": "HolePattern",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    remarks: Optional[str] = field(
        default=None,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 2000,
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
    hole_density: Optional[ReciprocalLengthMeasure] = field(
        default=None,
        metadata={
            "name": "HoleDensity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    hole_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "HoleCount",
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
