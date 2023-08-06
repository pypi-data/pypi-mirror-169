from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.event_info import EventInfo
from witsml20.extension_name_value import ExtensionNameValue
from witsml20.md_interval import MdInterval
from witsml20.perforation_status_history import PerforationStatusHistory
from witsml20.tvd_interval import TvdInterval

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class PerforationSetInterval:
    """
    The location/interval of the perforation set and its history.

    :ivar perforation_set_reference_id: Reference to a perforation set.
    :ivar perforation_set_md_interval: Overall measured depth interval
        for this perforation set.
    :ivar perforation_set_tvd_interval: Overall true vertical depth
        interval for this perforation set.
    :ivar event_history: The PerforationSetInterval event information.
    :ivar geology_feature_reference_id: Reference to a geology feature.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar perforation_status_history:
    :ivar uid: Unique identifier for this instance of
        PerforationSetInterval.
    """
    perforation_set_reference_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PerforationSetReferenceId",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    perforation_set_md_interval: Optional[MdInterval] = field(
        default=None,
        metadata={
            "name": "PerforationSetMdInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    perforation_set_tvd_interval: Optional[TvdInterval] = field(
        default=None,
        metadata={
            "name": "PerforationSetTvdInterval",
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
    perforation_status_history: List[PerforationStatusHistory] = field(
        default_factory=list,
        metadata={
            "name": "PerforationStatusHistory",
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
