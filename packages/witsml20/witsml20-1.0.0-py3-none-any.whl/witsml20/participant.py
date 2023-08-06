from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from witsml20.extension_name_value import ExtensionNameValue
from witsml20.member_object import MemberObject

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class Participant:
    """
    Information on WITSML objects used.

    :ivar ext_name_values: Extensions to the schema based on a name-
        value construct.
    :ivar participant:
    """
    ext_name_values: List[ExtensionNameValue] = field(
        default_factory=list,
        metadata={
            "name": "ExtNameValues",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    participant: List[MemberObject] = field(
        default_factory=list,
        metadata={
            "name": "Participant",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
