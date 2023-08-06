from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.custom_data import CustomData
from witsml20.force_measure import ForceMeasure
from witsml20.jar_action import JarAction
from witsml20.jar_type import JarType

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class Jar:
    """WITSML - Tubular Jar Component Schema. Captures information about jars, which are mechanical or hydraulic devices used in the drill stem to deliver an impact load to another component of the drill stem, especially when that component is stuck.

    :ivar for_up_set: Up set force.
    :ivar for_down_set: Down set force.
    :ivar for_up_trip: Up trip force.
    :ivar for_down_trip: Down trip force.
    :ivar for_pmp_open: Pump open force.
    :ivar for_seal_fric: Seal friction force.
    :ivar type_jar: The kind of jar.
    :ivar jar_action: The jar action.
    :ivar extension_any:
    """
    for_up_set: Optional[ForceMeasure] = field(
        default=None,
        metadata={
            "name": "ForUpSet",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    for_down_set: Optional[ForceMeasure] = field(
        default=None,
        metadata={
            "name": "ForDownSet",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    for_up_trip: Optional[ForceMeasure] = field(
        default=None,
        metadata={
            "name": "ForUpTrip",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    for_down_trip: Optional[ForceMeasure] = field(
        default=None,
        metadata={
            "name": "ForDownTrip",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    for_pmp_open: Optional[ForceMeasure] = field(
        default=None,
        metadata={
            "name": "ForPmpOpen",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    for_seal_fric: Optional[ForceMeasure] = field(
        default=None,
        metadata={
            "name": "ForSealFric",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    type_jar: Optional[JarType] = field(
        default=None,
        metadata={
            "name": "TypeJar",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    jar_action: Optional[JarAction] = field(
        default=None,
        metadata={
            "name": "JarAction",
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
