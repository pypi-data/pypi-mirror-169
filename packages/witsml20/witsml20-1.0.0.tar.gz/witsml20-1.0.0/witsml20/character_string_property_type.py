from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from witsml20.ci_date_type_code import CiDateTypeCode
from witsml20.ci_on_line_function_code import CiOnLineFunctionCode
from witsml20.ci_presentation_form_code import CiPresentationFormCode
from witsml20.ci_role_code import CiRoleCode
from witsml20.dq_evaluation_method_type_code import DqEvaluationMethodTypeCode
from witsml20.nil_reason_enumeration_value import NilReasonEnumerationValue

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class CharacterStringPropertyType:
    class Meta:
        name = "CharacterString_PropertyType"

    dq_evaluation_method_type_code: Optional[DqEvaluationMethodTypeCode] = field(
        default=None,
        metadata={
            "name": "DQ_EvaluationMethodTypeCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    ci_presentation_form_code: Optional[CiPresentationFormCode] = field(
        default=None,
        metadata={
            "name": "CI_PresentationFormCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    ci_role_code: Optional[CiRoleCode] = field(
        default=None,
        metadata={
            "name": "CI_RoleCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    ci_on_line_function_code: Optional[CiOnLineFunctionCode] = field(
        default=None,
        metadata={
            "name": "CI_OnLineFunctionCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    ci_date_type_code: Optional[CiDateTypeCode] = field(
        default=None,
        metadata={
            "name": "CI_DateTypeCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    character_string: Optional[str] = field(
        default=None,
        metadata={
            "name": "CharacterString",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gco",
        }
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "namespace": "http://www.isotc211.org/2005/gco",
            "pattern": r"other:\w{2,}",
        }
    )
