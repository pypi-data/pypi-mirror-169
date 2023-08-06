from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.existence_kind import ExistenceKind
from witsml20.extension_name_value import ExtensionNameValue
from witsml20.length_measure import LengthMeasure
from witsml20.md_interval import MdInterval

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class SurveySection:
    """
    Survey Section Component Schema.

    :ivar sequence: Order in which the program sections are or were
        executed.
    :ivar name: Name of the survey program section.
    :ivar md_interval:
    :ivar name_survey_company: Company who will run or has run the
        survey tool.
    :ivar name_tool: Name of survey tool used in this section.
    :ivar type_tool: Type of tool used.
    :ivar model_error: Error model used to calculate the ellipses of
        uncertainty.
    :ivar overwrite: Higher index trajectory takes precedence over
        overlapping section of previous trajectory?   Values are "true"
        (or "1") and "false" (or "0"). Normally, this is true.
    :ivar frequency_mx: Maximum allowable depth frequency for survey
        stations for this survey run.
    :ivar item_state: The item state for the data object.
    :ivar comments: Comments and remarks.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar uid: Unique identifier of this instance of SurveySection.
    """
    sequence: Optional[int] = field(
        default=None,
        metadata={
            "name": "Sequence",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "min_inclusive": 0,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    md_interval: Optional[MdInterval] = field(
        default=None,
        metadata={
            "name": "MdInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    name_survey_company: Optional[str] = field(
        default=None,
        metadata={
            "name": "NameSurveyCompany",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    name_tool: Optional[str] = field(
        default=None,
        metadata={
            "name": "NameTool",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    type_tool: Optional[str] = field(
        default=None,
        metadata={
            "name": "TypeTool",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    model_error: Optional[str] = field(
        default=None,
        metadata={
            "name": "ModelError",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    overwrite: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Overwrite",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    frequency_mx: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "FrequencyMx",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    item_state: Optional[ExistenceKind] = field(
        default=None,
        metadata={
            "name": "ItemState",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    comments: Optional[str] = field(
        default=None,
        metadata={
            "name": "Comments",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 2000,
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
    uid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 64,
        }
    )
