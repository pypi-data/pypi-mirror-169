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
class SlotsInterval:
    """
    The location/interval of the slots and the history.

    :ivar string_equipment_reference_id: Reference to an equipment
        string, which is the equipment (e.g., tubing, gravel pack
        screens, etc.) that compose the completion.
    :ivar slotted_md_interval: Slotted measured depth interval for this
        completion.
    :ivar slotted_tvd_interval: Slotted true vertical depth interval for
        this completion.
    :ivar event_history: The SlotsInterval event information.
    :ivar geology_feature_ref_id: Reference to a geology feature.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar status_history:
    :ivar uid: Unique identifier for this instance of SlotsInterval.
    """
    string_equipment_reference_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "StringEquipmentReferenceId",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    slotted_md_interval: Optional[MdInterval] = field(
        default=None,
        metadata={
            "name": "SlottedMdInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    slotted_tvd_interval: Optional[TvdInterval] = field(
        default=None,
        metadata={
            "name": "SlottedTvdInterval",
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
    geology_feature_ref_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "GeologyFeatureRefID",
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
