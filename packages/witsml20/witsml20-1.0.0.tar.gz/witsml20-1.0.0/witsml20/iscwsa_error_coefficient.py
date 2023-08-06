from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.abstract_iscwsa_error_coefficient import AbstractIscwsaErrorCoefficient
from witsml20.extension_name_value import ExtensionNameValue

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class IscwsaErrorCoefficient:
    """
    Describes what survey measurement or value the error term applies to.

    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar abstract_iscwsa_error_coefficient:
    :ivar uid: Unique identifier for this instance of
        IscwsaErrorCoefficient.
    """
    extension_name_value: List[ExtensionNameValue] = field(
        default_factory=list,
        metadata={
            "name": "ExtensionNameValue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    abstract_iscwsa_error_coefficient: List[AbstractIscwsaErrorCoefficient] = field(
        default_factory=list,
        metadata={
            "name": "AbstractIscwsaErrorCoefficient",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "min_occurs": 1,
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
