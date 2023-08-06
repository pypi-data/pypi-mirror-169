from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.extension_name_value import ExtensionNameValue

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class IscwsaNameAndDescription:
    """A generic type which captures a name and a description of something.

    The semantics of the something is defined by the parent element.

    :ivar name: The name of the item.
    :ivar description: A textual description of the item.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar uid: Unique identifier for this instance of
        IscwsaNameAndDescription.
    """
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "max_length": 2000,
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
