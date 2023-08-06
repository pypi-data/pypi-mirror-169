from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.event_info import EventInfo
from witsml20.extension_name_value import ExtensionNameValue
from witsml20.interval_status_history import IntervalStatusHistory
from witsml20.md_interval import MdInterval
from witsml20.tvd_interval import TvdInterval

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class GravelPackInterval:
    """
    The location/interval of the gravel pack, including its history.

    :ivar downhole_string_reference_id: Reference to the downhole string
        that denotes the interval of the gravel pack.
    :ivar gravel_pack_md_interval: Gravel packed measured depth interval
        for this completion.
    :ivar gravel_pack_tvd_interval: Gravel packed true vertical depth
        interval for this completion.
    :ivar event_history: The contactInterval event information.
    :ivar geology_feature_reference_id: Reference to a geology feature.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar status_history:
    :ivar uid: Unique identifier for this instance of
        GravelPackInterval.
    """
    downhole_string_reference_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "DownholeStringReferenceId",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    gravel_pack_md_interval: Optional[MdInterval] = field(
        default=None,
        metadata={
            "name": "GravelPackMdInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    gravel_pack_tvd_interval: Optional[TvdInterval] = field(
        default=None,
        metadata={
            "name": "GravelPackTvdInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
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
    geology_feature_reference_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "GeologyFeatureReferenceId",
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
    status_history: List[IntervalStatusHistory] = field(
        default_factory=list,
        metadata={
            "name": "StatusHistory",
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
