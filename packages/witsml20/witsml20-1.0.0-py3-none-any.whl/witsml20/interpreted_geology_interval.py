from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.citation import Citation
from witsml20.custom_data import CustomData
from witsml20.existence_kind import ExistenceKind
from witsml20.extension_name_value import ExtensionNameValue
from witsml20.geochronological_unit import GeochronologicalUnit
from witsml20.interpreted_interval_lithology import InterpretedIntervalLithology
from witsml20.lithostratigraphic_unit import LithostratigraphicUnit
from witsml20.md_interval import MdInterval
from witsml20.object_alias import ObjectAlias

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class InterpretedGeologyInterval:
    """Represents a depth interval along the wellbore which contains a single
    interpreted lithology type. It can be used to:

    - carry information about geochronology and lithostratigraphy
    - create a pre-well geological prognosis with chronostratigraphic, lithostratigraphic, and lithology entries.

    :ivar aliases:
    :ivar md_interval: The measured depth interval which is described by
        this interpreted geology.
    :ivar custom_data:
    :ivar extension_name_value:
    :ivar object_version:
    :ivar schema_version:
    :ivar uuid:
    :ivar existence_kind: A lifecycle state like actual, required,
        planned, predicted, etc. This is used to qualify any top-level
        element (from Epicentre -2.1).
    :ivar citation: An ISO 19115 EIP-derived set of metadata attached to
        ensure the traceability of the InterpretedGeologyInterval.
    :ivar geochronological_unit: The name of a Geochronology, with the
        "kind" attribute specifying the geochronological time span.
    :ivar lithostratigraphic_unit: Specifies the unit of
        lithostratigraphy.
    :ivar interpreted_lithology:
    :ivar uid: Unique identifier for this instance of
        InterpretedGeologyInterval.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/witsmlv2"

    aliases: List[ObjectAlias] = field(
        default_factory=list,
        metadata={
            "name": "Aliases",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
        }
    )
    md_interval: Optional[MdInterval] = field(
        default=None,
        metadata={
            "name": "MdInterval",
            "type": "Element",
            "required": True,
        }
    )
    custom_data: Optional[CustomData] = field(
        default=None,
        metadata={
            "name": "CustomData",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
        }
    )
    extension_name_value: List[ExtensionNameValue] = field(
        default_factory=list,
        metadata={
            "name": "ExtensionNameValue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
        }
    )
    object_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "objectVersion",
            "type": "Attribute",
            "max_length": 64,
        }
    )
    schema_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "schemaVersion",
            "type": "Attribute",
            "required": True,
            "max_length": 64,
        }
    )
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    existence_kind: Optional[ExistenceKind] = field(
        default=None,
        metadata={
            "name": "existenceKind",
            "type": "Attribute",
        }
    )
    citation: Optional[Citation] = field(
        default=None,
        metadata={
            "name": "Citation",
            "type": "Element",
        }
    )
    geochronological_unit: List[GeochronologicalUnit] = field(
        default_factory=list,
        metadata={
            "name": "GeochronologicalUnit",
            "type": "Element",
        }
    )
    lithostratigraphic_unit: List[LithostratigraphicUnit] = field(
        default_factory=list,
        metadata={
            "name": "LithostratigraphicUnit",
            "type": "Element",
        }
    )
    interpreted_lithology: Optional[InterpretedIntervalLithology] = field(
        default=None,
        metadata={
            "name": "InterpretedLithology",
            "type": "Element",
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
