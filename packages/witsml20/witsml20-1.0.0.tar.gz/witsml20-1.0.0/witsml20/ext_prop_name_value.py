from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class ExtPropNameValue:
    """
    Name-value extensions for the equipment property.

    :ivar name: A string representing the name of property.
    :ivar value: A value string representing the units of measure of the
        value.
    :ivar uid: Unique identifier for this instance of ExtPropNameValue.
    """
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 2000,
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
