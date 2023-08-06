from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.abstract_event_extension import AbstractEventExtension
from witsml20.abstract_object import AbstractObject
from witsml20.data_object_reference import DataObjectReference
from witsml20.day_cost import DayCost
from witsml20.downhole_component_reference import DownholeComponentReference
from witsml20.drill_activity_code import DrillActivityCode
from witsml20.event_type import EventType
from witsml20.md_interval import MdInterval
from witsml20.participant import Participant
from witsml20.time_measure import TimeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class WellCmledger(AbstractObject):
    """
    Information regarding details of Jobs &amp; Events.

    :ivar parent_event_id: Parent event reference id.
    :ivar dtim_start: Date and time that activities started.
    :ivar dtim_end: Date and time that activities were completed.
    :ivar duration: The activity duration (commonly in hours).
    :ivar md_interval: Measured depth interval for this activity.
    :ivar event_order: Order number of event.
    :ivar rig_id: Rig reference id.
    :ivar activity_code: Activity code
    :ivar type: Comment on type of this event, either referring to a job
        type or an  activity type e.g. a safety meeting.
    :ivar is_plan: True if planned.
    :ivar work_order_id: Extension event for work order id.
    :ivar business_associate: Service company or business
    :ivar responsible_person: Name or information about person
        responsible who is implementing the service or job.
    :ivar contact: Contact name or person to get in touch with. Might
        not necessarily be the person responsible.
    :ivar nonproductive: True if event is not productive.
    :ivar trouble: True if event implies is in-trouble
    :ivar preventive_maintenance: True of event is for preventive
        maintenance
    :ivar unplanned: True if there is no planning infomation for this
        activity.
    :ivar phase: Phase (large activity classification) e.g. Drill
        Surface Hole.
    :ivar comment: Comment on this ledger
    :ivar description: Description of this ledger
    :ivar wellbore:
    :ivar event_extension:
    :ivar cost:
    :ivar event_type:
    :ivar downhole_component_reference:
    :ivar participant:
    """
    class Meta:
        name = "WellCMLedger"
        namespace = "http://www.energistics.org/energyml/data/witsmlv2"

    parent_event_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ParentEventID",
            "type": "Element",
            "max_length": 64,
        }
    )
    dtim_start: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimStart",
            "type": "Element",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    dtim_end: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimEnd",
            "type": "Element",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    duration: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "Duration",
            "type": "Element",
        }
    )
    md_interval: Optional[MdInterval] = field(
        default=None,
        metadata={
            "name": "MdInterval",
            "type": "Element",
        }
    )
    event_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "EventOrder",
            "type": "Element",
        }
    )
    rig_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "RigID",
            "type": "Element",
            "max_length": 64,
        }
    )
    activity_code: Optional[DrillActivityCode] = field(
        default=None,
        metadata={
            "name": "ActivityCode",
            "type": "Element",
        }
    )
    type: Optional[EventType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
        }
    )
    is_plan: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsPlan",
            "type": "Element",
        }
    )
    work_order_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "WorkOrderID",
            "type": "Element",
            "max_length": 64,
        }
    )
    business_associate: Optional[str] = field(
        default=None,
        metadata={
            "name": "BusinessAssociate",
            "type": "Element",
            "max_length": 64,
        }
    )
    responsible_person: Optional[str] = field(
        default=None,
        metadata={
            "name": "ResponsiblePerson",
            "type": "Element",
            "max_length": 64,
        }
    )
    contact: Optional[str] = field(
        default=None,
        metadata={
            "name": "Contact",
            "type": "Element",
            "max_length": 64,
        }
    )
    nonproductive: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Nonproductive",
            "type": "Element",
        }
    )
    trouble: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Trouble",
            "type": "Element",
        }
    )
    preventive_maintenance: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PreventiveMaintenance",
            "type": "Element",
        }
    )
    unplanned: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Unplanned",
            "type": "Element",
        }
    )
    phase: Optional[str] = field(
        default=None,
        metadata={
            "name": "Phase",
            "type": "Element",
            "max_length": 64,
        }
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "name": "Comment",
            "type": "Element",
            "max_length": 2000,
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "max_length": 2000,
        }
    )
    wellbore: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Wellbore",
            "type": "Element",
            "required": True,
        }
    )
    event_extension: List[AbstractEventExtension] = field(
        default_factory=list,
        metadata={
            "name": "EventExtension",
            "type": "Element",
        }
    )
    cost: List[DayCost] = field(
        default_factory=list,
        metadata={
            "name": "Cost",
            "type": "Element",
        }
    )
    event_type: Optional[EventType] = field(
        default=None,
        metadata={
            "name": "EventType",
            "type": "Element",
        }
    )
    downhole_component_reference: Optional[DownholeComponentReference] = field(
        default=None,
        metadata={
            "name": "DownholeComponentReference",
            "type": "Element",
        }
    )
    participant: Optional[Participant] = field(
        default=None,
        metadata={
            "name": "Participant",
            "type": "Element",
        }
    )
