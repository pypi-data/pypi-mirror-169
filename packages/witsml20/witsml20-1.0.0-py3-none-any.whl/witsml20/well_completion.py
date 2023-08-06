from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.abstract_object import AbstractObject
from witsml20.completion_status import CompletionStatus
from witsml20.completion_status_history import CompletionStatusHistory
from witsml20.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class WellCompletion(AbstractObject):
    """
    Information regarding  a wellhead stream with one or more wellbore
    completions (completed zones) in the well.

    :ivar field_id: Field ID.
    :ivar field_code: Field code.
    :ivar field_type: Field type.
    :ivar effective_date: Field date.
    :ivar expired_date: Expiration date.
    :ivar e_p_rights_id: Documents exploration and production rights.
    :ivar current_status: Status (active, planned, suspended, testing,
        etc.) of the well completion.
    :ivar status_date: Timestamp for when this status was established.
    :ivar status_history:
    :ivar well:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/witsmlv2"

    field_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "FieldID",
            "type": "Element",
            "max_length": 64,
        }
    )
    field_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "FieldCode",
            "type": "Element",
            "max_length": 64,
        }
    )
    field_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "FieldType",
            "type": "Element",
            "max_length": 64,
        }
    )
    effective_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "EffectiveDate",
            "type": "Element",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    expired_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "ExpiredDate",
            "type": "Element",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    e_p_rights_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "E_P_RightsID",
            "type": "Element",
            "max_length": 64,
        }
    )
    current_status: Optional[CompletionStatus] = field(
        default=None,
        metadata={
            "name": "CurrentStatus",
            "type": "Element",
        }
    )
    status_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "StatusDate",
            "type": "Element",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    status_history: List[CompletionStatusHistory] = field(
        default_factory=list,
        metadata={
            "name": "StatusHistory",
            "type": "Element",
        }
    )
    well: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Well",
            "type": "Element",
            "required": True,
        }
    )
