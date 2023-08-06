from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.custom_data import CustomData
from witsml20.extension_name_value import ExtensionNameValue
from witsml20.length_measure import LengthMeasure
from witsml20.nozzle_type import NozzleType

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class Nozzle:
    """
    Nozzle Component Schema.

    :ivar index: Index if this is an indexed object.
    :ivar dia_nozzle: Nozzle diameter.
    :ivar type_nozzle: Nozzle type.
    :ivar len: Length of the nozzle.
    :ivar orientation: Nozzle orientation.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar extension_any:
    :ivar uid: Unique identifier for this instance of Nozzle
    """
    index: Optional[int] = field(
        default=None,
        metadata={
            "name": "Index",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    dia_nozzle: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "DiaNozzle",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    type_nozzle: Optional[NozzleType] = field(
        default=None,
        metadata={
            "name": "TypeNozzle",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    len: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "Len",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    orientation: Optional[str] = field(
        default=None,
        metadata={
            "name": "Orientation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
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
    uid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 64,
        }
    )
