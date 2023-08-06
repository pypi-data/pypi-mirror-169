from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.abstract_event_extension import AbstractEventExtension
from witsml20.custom_data import CustomData
from witsml20.extension_name_value import ExtensionNameValue
from witsml20.length_measure import LengthMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class CleanFillExtension(AbstractEventExtension):
    """
    Information on clean fill event.

    :ivar fill_cleaning_method: method of fill and cleaning
    :ivar tool_size: the size of the tool
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar extension_any:
    """
    fill_cleaning_method: Optional[str] = field(
        default=None,
        metadata={
            "name": "FillCleaningMethod",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    tool_size: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "ToolSize",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
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
    extension_any: Optional[CustomData] = field(
        default=None,
        metadata={
            "name": "ExtensionAny",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
