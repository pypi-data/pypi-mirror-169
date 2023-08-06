from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.event_info import EventInfo
from witsml20.length_measure import LengthMeasure
from witsml20.md_interval import MdInterval
from witsml20.perforation_tool_type import PerforationToolType
from witsml20.plane_angle_measure import PlaneAngleMeasure
from witsml20.pressure_measure import PressureMeasure
from witsml20.reciprocal_length_measure import ReciprocalLengthMeasure
from witsml20.tvd_interval import TvdInterval

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class PerforationSet:
    """
    Information regarding a collection of perforations.

    :ivar borehole_string_reference_id: Reference to the borehole that
        contains the perf set.
    :ivar downhole_string_reference_id: Reference to the downhole
        string.
    :ivar md_interval: Measured depth interval for the entire
        perforation set.
    :ivar tvd_interval: The true vertical depth of the entire
        perforation set.
    :ivar hole_diameter: The diameter of the perf holes.
    :ivar hole_angle: The angle of the holes.
    :ivar hole_pattern: The pattern of the holes.
    :ivar hole_density: The density of the holes.
    :ivar hole_count: The number of holes.
    :ivar friction_factor: The friction factor of each perforation set.
    :ivar friction_pres: The friction pressure for the perforation set.
    :ivar discharge_coefficient: A coefficient used in the equation for
        calculation of pressure drop across a perforation set.
    :ivar perforation_tool: The type of perforation tool.
    :ivar perforation_penetration: The penetration length of
        perforation.
    :ivar crush_zone_diameter: The diameter of the crushed zone.
    :ivar crush_damage_ratio: The ratio value of crash damage.
    :ivar perforation_date: The original perforation date.
    :ivar permanent_remarks: Remarks regarding this perforation set.
    :ivar event_history:
    :ivar uid: Unique identifier for this instance of PerforationSet.
    """
    borehole_string_reference_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "BoreholeStringReferenceId",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    downhole_string_reference_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DownholeStringReferenceId",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
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
    friction_factor: Optional[float] = field(
        default=None,
        metadata={
            "name": "FrictionFactor",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    friction_pres: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "FrictionPres",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    discharge_coefficient: Optional[float] = field(
        default=None,
        metadata={
            "name": "DischargeCoefficient",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    perforation_tool: Optional[PerforationToolType] = field(
        default=None,
        metadata={
            "name": "PerforationTool",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    perforation_penetration: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "PerforationPenetration",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    crush_zone_diameter: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "CrushZoneDiameter",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    crush_damage_ratio: Optional[str] = field(
        default=None,
        metadata={
            "name": "CrushDamageRatio",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    perforation_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "PerforationDate",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    permanent_remarks: Optional[str] = field(
        default=None,
        metadata={
            "name": "PermanentRemarks",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 2000,
        }
    )
    event_history: Optional[EventInfo] = field(
        default=None,
        metadata={
            "name": "EventHistory",
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
