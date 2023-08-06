from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.custom_data import CustomData
from witsml20.hole_opener_type import HoleOpenerType
from witsml20.length_measure import LengthMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class HoleOpener:
    """Hole Opener Component Schema.

    Describes the hole-opener tool (often called a ‘reamer’) used on the
    tubular string.

    :ivar type_hole_opener: Under reamer or fixed blade.
    :ivar num_cutter: Number of cutters on the tool.
    :ivar manufacturer: Manufacturer or supplier of the tool.
    :ivar dia_hole_opener: Diameter of the reamer.
    :ivar extension_any:
    """
    type_hole_opener: Optional[HoleOpenerType] = field(
        default=None,
        metadata={
            "name": "TypeHoleOpener",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    num_cutter: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumCutter",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    manufacturer: Optional[str] = field(
        default=None,
        metadata={
            "name": "Manufacturer",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    dia_hole_opener: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "DiaHoleOpener",
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
