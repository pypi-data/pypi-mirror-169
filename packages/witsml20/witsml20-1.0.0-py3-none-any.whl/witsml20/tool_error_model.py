from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.abstract_object import AbstractObject
from witsml20.iscwsa_authorization_data import IscwsaAuthorizationData
from witsml20.iscwsa_error_term_value import IscwsaErrorTermValue
from witsml20.iscwsa_model_parameters import IscwsaModelParameters
from witsml20.iscwsa_survey_tool_operating_condition import IscwsaSurveyToolOperatingCondition
from witsml20.iscwsa_survey_tool_operating_interval import IscwsaSurveyToolOperatingInterval
from witsml20.type_survey_tool import TypeSurveyTool

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class ToolErrorModel(AbstractObject):
    """Used to define a surveying tool error model.

    This object is globally unique.

    :ivar type_survey_tool: The type of tool used for the measurements.
        This is the same list as defined for a trajectoryStation.
    :ivar use_error_term_set: Reference to the toolErrorTermSet object
        that contains the error terms used in this model.
    :ivar authorization:
    :ivar operating_condition:
    :ivar operating_interval:
    :ivar model_parameters:
    :ivar error_term_value:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/witsmlv2"

    type_survey_tool: Optional[TypeSurveyTool] = field(
        default=None,
        metadata={
            "name": "TypeSurveyTool",
            "type": "Element",
        }
    )
    use_error_term_set: Optional[str] = field(
        default=None,
        metadata={
            "name": "UseErrorTermSet",
            "type": "Element",
            "max_length": 64,
        }
    )
    authorization: Optional[IscwsaAuthorizationData] = field(
        default=None,
        metadata={
            "name": "Authorization",
            "type": "Element",
        }
    )
    operating_condition: List[IscwsaSurveyToolOperatingCondition] = field(
        default_factory=list,
        metadata={
            "name": "OperatingCondition",
            "type": "Element",
        }
    )
    operating_interval: List[IscwsaSurveyToolOperatingInterval] = field(
        default_factory=list,
        metadata={
            "name": "OperatingInterval",
            "type": "Element",
        }
    )
    model_parameters: Optional[IscwsaModelParameters] = field(
        default=None,
        metadata={
            "name": "ModelParameters",
            "type": "Element",
        }
    )
    error_term_value: List[IscwsaErrorTermValue] = field(
        default_factory=list,
        metadata={
            "name": "ErrorTermValue",
            "type": "Element",
            "min_occurs": 1,
        }
    )
