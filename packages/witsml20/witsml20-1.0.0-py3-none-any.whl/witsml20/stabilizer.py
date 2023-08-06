from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.blade_shape_type import BladeShapeType
from witsml20.blade_type import BladeType
from witsml20.custom_data import CustomData
from witsml20.extension_name_value import ExtensionNameValue
from witsml20.length_measure import LengthMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class Stabilizer:
    """Tubular Stablizer Component Schema.

    Captures dimension and operation information about stabilizers used
    in the tubular string.

    :ivar len_blade: Length of the blade.
    :ivar len_blade_gauge: Gauge Length of the blade. That is, the
        length of the blade measured at the OdBladeMx.
    :ivar od_blade_mx: Maximum outer diameter of the blade.
    :ivar od_blade_mn: Minimum outer diameter of the blade.
    :ivar dist_blade_bot: Distance of the blade bottom from the bottom
        of the component.
    :ivar shape_blade: Blade shape.
    :ivar fact_fric: Friction factor.
    :ivar type_blade: Blade type.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar extension_any:
    :ivar uid: Unique identifier for this instance of Stabilizer.
    """
    len_blade: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "LenBlade",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    len_blade_gauge: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "LenBladeGauge",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    od_blade_mx: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "OdBladeMx",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    od_blade_mn: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "OdBladeMn",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    dist_blade_bot: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "DistBladeBot",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    shape_blade: Optional[BladeShapeType] = field(
        default=None,
        metadata={
            "name": "ShapeBlade",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    fact_fric: Optional[float] = field(
        default=None,
        metadata={
            "name": "FactFric",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    type_blade: Optional[BladeType] = field(
        default=None,
        metadata={
            "name": "TypeBlade",
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
    uid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 64,
        }
    )
