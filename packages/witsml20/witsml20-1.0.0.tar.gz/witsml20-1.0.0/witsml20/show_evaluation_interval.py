from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.citation import Citation
from witsml20.custom_data import CustomData
from witsml20.existence_kind import ExistenceKind
from witsml20.extension_name_value import ExtensionNameValue
from witsml20.md_interval import MdInterval
from witsml20.object_alias import ObjectAlias
from witsml20.show_fluid import ShowFluid
from witsml20.show_rating import ShowRating

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class ShowEvaluationInterval:
    """An interpretation of the overall hydrocarbon show derived from analysis
    of individual show tests on cuttings samples.

    An interval in the wellbore for which data is manually entered by
    the wellsite geologist or mud logger as an interpretation of the
    hydrocarbon show along the wellbore, based on the raw readings from
    one or more show analyses of individual show tests on cuttings
    samples.

    :ivar aliases:
    :ivar md_interval: The measured depth interval over which the show
        is evaluated.
    :ivar custom_data:
    :ivar extension_name_value:
    :ivar object_version:
    :ivar schema_version:
    :ivar uuid:
    :ivar existence_kind: A lifecycle state like actual, required,
        planned, predicted, etc. This is used to qualify any top-level
        element (from Epicentre -2.1).
    :ivar citation: An ISO 19115 EIP-derived set of metadata attached to
        ensure the traceability of the ShowEvaluationInterval
    :ivar show_fluid: Gas or oil exhibited at the show interval.
    :ivar show_rating: Quality of the fluid showing at this interval.
    :ivar uid: Unique identifier for this instance of
        ShowEvaluationInterval.
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
    show_fluid: Optional[ShowFluid] = field(
        default=None,
        metadata={
            "name": "ShowFluid",
            "type": "Element",
            "required": True,
        }
    )
    show_rating: Optional[ShowRating] = field(
        default=None,
        metadata={
            "name": "ShowRating",
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
