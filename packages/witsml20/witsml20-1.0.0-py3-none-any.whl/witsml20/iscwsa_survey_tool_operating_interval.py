from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.extension_name_value import ExtensionNameValue
from witsml20.length_per_time_measure import LengthPerTimeMeasure
from witsml20.plane_angle_measure import PlaneAngleMeasure
from witsml20.survey_tool_operating_mode import SurveyToolOperatingMode
from witsml20.time_measure import TimeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class IscwsaSurveyToolOperatingInterval:
    """Inclination interval for a particular operating mode.

    Intervals may overlap to suppress mode flip-flopping, but should
    cover the entire valid range of the tool.

    :ivar mode: Tool operating mode over this interval.
    :ivar start: Inclination at which the mode begins.
    :ivar end: Inclination at which the mode terminates.
    :ivar speed: Running speed for continuous surveys.
    :ivar sample_rate: Time between survey samples for continuous
        surveys.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar uid: Unique identifier for this instance of
        IscwsaSurveyToolOperatingInterval.
    """
    mode: Optional[SurveyToolOperatingMode] = field(
        default=None,
        metadata={
            "name": "Mode",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    start: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "Start",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    end: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "End",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    speed: Optional[LengthPerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "Speed",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    sample_rate: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "SampleRate",
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
