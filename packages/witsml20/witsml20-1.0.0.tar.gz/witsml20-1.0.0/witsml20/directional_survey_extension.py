from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.abstract_event_extension import AbstractEventExtension
from witsml20.custom_data import CustomData
from witsml20.extension_name_value import ExtensionNameValue

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class DirectionalSurveyExtension(AbstractEventExtension):
    """
    Information on directional survey event.

    :ivar trajectory_ref_id: Reference to trajectory
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar extension_any:
    """
    trajectory_ref_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrajectoryRefID",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
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
