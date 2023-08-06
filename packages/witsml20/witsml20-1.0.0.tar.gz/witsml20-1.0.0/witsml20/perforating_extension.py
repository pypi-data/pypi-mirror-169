from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.abstract_event_extension import AbstractEventExtension
from witsml20.custom_data import CustomData
from witsml20.perforating import Perforating

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class PerforatingExtension(AbstractEventExtension):
    """
    Information on the perforating event.

    :ivar perforation_set_ref_id: The perforationSet reference ID.
    :ivar extension_any:
    :ivar perforating:
    """
    perforation_set_ref_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PerforationSetRefID",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    extension_any: Optional[CustomData] = field(
        default=None,
        metadata={
            "name": "ExtensionAny",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    perforating: List[Perforating] = field(
        default_factory=list,
        metadata={
            "name": "Perforating",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
