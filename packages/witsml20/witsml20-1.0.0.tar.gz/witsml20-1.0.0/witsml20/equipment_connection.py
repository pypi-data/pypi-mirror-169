from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.abstract_connection_type import AbstractConnectionType
from witsml20.connection import Connection
from witsml20.connection_form_type import ConnectionFormType
from witsml20.length_measure import LengthMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class EquipmentConnection(Connection):
    """
    Information detailing the connection between two components.

    :ivar radial_offset: Measurement of radial offset.
    :ivar connection_form: The form of connection: box or pin.
    :ivar connection_upset: Connection upset.
    :ivar connection_type:
    :ivar string_equipment_reference_uid: Reference to the string
        equipment.
    """
    radial_offset: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "RadialOffset",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    connection_form: Optional[ConnectionFormType] = field(
        default=None,
        metadata={
            "name": "ConnectionForm",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    connection_upset: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConnectionUpset",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    connection_type: Optional[AbstractConnectionType] = field(
        default=None,
        metadata={
            "name": "ConnectionType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    string_equipment_reference_uid: Optional[str] = field(
        default=None,
        metadata={
            "name": "stringEquipmentReferenceUid",
            "type": "Attribute",
            "required": True,
            "max_length": 64,
        }
    )
