from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.abstract_object import AbstractObject
from witsml20.data_object_reference import DataObjectReference
from witsml20.failing_rule import FailingRule
from witsml20.index_range import IndexRange

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class DataAssuranceRecord(AbstractObject):
    """
    A little XML document describing whether or not a particular data object
    conforms with a pre-defined policy which consists of at least one rule.

    :ivar policy_id: Identifier of the policy whose conformance is being
        described.
    :ivar policy_name: Human-readable name of the policy
    :ivar referenced_element_name: If the Policy applies to a single
        element within the referenced data object this attribute holds
        its element name.
    :ivar referenced_element_uid: If the Policy applies to a single
        occurrence of a recurring element within the referenced data
        object this attribute holds its uid. The name of the recurring
        element would be in the ReferencedElementName.
    :ivar origin: Agent which checked the data for conformance with the
        policy. This could be a person or an automated computer process
        or any number of other things.
    :ivar conformance: Yes/no flag indicating whether this particular
        data ???? conforms with the policy or not.
    :ivar date: Date the policy was last checked. This is the date for
        which the Conformance value is valid.
    :ivar comment:
    :ivar failing_rules:
    :ivar index_range:
    :ivar referenced_data:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/commonv2"

    policy_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PolicyId",
            "type": "Element",
            "required": True,
            "max_length": 64,
        }
    )
    policy_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "PolicyName",
            "type": "Element",
            "max_length": 2000,
        }
    )
    referenced_element_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReferencedElementName",
            "type": "Element",
            "max_length": 64,
        }
    )
    referenced_element_uid: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReferencedElementUid",
            "type": "Element",
            "max_length": 64,
        }
    )
    origin: Optional[str] = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Element",
            "required": True,
        }
    )
    conformance: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Conformance",
            "type": "Element",
            "required": True,
        }
    )
    date: Optional[str] = field(
        default=None,
        metadata={
            "name": "Date",
            "type": "Element",
            "required": True,
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "name": "Comment",
            "type": "Element",
        }
    )
    failing_rules: List[FailingRule] = field(
        default_factory=list,
        metadata={
            "name": "FailingRules",
            "type": "Element",
        }
    )
    index_range: Optional[IndexRange] = field(
        default=None,
        metadata={
            "name": "IndexRange",
            "type": "Element",
        }
    )
    referenced_data: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "ReferencedData",
            "type": "Element",
            "required": True,
        }
    )
