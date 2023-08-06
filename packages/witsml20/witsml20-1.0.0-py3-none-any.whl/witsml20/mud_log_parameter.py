from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.citation import Citation
from witsml20.md_interval import MdInterval

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class MudLogParameter:
    """
    Information around the mud log: type, time taken, top and bottom depth,
    pressure gradient, etc.

    :ivar md_interval: Measured depth interval that is the focus of this
        parameter.
    :ivar citation: An ISO 19115 EIP-derived set of metadata attached to
        ensure the traceability of the MudLogParameter.
    :ivar comments: Description or secondary qualifier pertaining to
        MudlogParameter or to Value attribute.
    :ivar uid: Unique identifier for this instance of MudLogParameter.
    """
    md_interval: Optional[MdInterval] = field(
        default=None,
        metadata={
            "name": "MdInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    citation: Optional[Citation] = field(
        default=None,
        metadata={
            "name": "Citation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    comments: Optional[str] = field(
        default=None,
        metadata={
            "name": "Comments",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
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
