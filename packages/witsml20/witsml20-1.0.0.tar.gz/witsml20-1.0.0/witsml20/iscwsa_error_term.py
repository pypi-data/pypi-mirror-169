from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.error_term_source import ErrorTermSource
from witsml20.extension_name_value import ExtensionNameValue
from witsml20.iscwsa_error_coefficient import IscwsaErrorCoefficient
from witsml20.measure_class import MeasureType
from witsml20.survey_tool_operating_mode import SurveyToolOperatingMode

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class IscwsaErrorTerm:
    """
    Captures the reference error terms that are included in error models using
    ErrorTermValues.

    :ivar name: This is the unique mnemonic for this term, e.g., "ABIX"
        or "DECR".
    :ivar type: The class of the error source.
    :ivar measure_class: The kind of quantity that the term represents.
        This constrains the unit that can be used for any
        errorTermValues.
    :ivar label: Human-readable name for the term, may be presented in
        application software. E.g., "MWD: X-Acceleromter Bias with
        Z-Axis Corr."
    :ivar description: Human-readable name for the term. It may be
        presented in application software, e.g., "MWD: X-Acceleromter
        Bias with Z-Axis Corr."
    :ivar operating_mode: Operating mode that is valid for this error
        term. In the absence of this element assume "stationary".
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar error_coefficient:
    :ivar uid: Unique identifier for this instance of IscwsaErrorTerm.
    """
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    type: Optional[ErrorTermSource] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    measure_class: Optional[MeasureType] = field(
        default=None,
        metadata={
            "name": "MeasureClass",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    label: Optional[str] = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 2000,
        }
    )
    operating_mode: List[SurveyToolOperatingMode] = field(
        default_factory=list,
        metadata={
            "name": "OperatingMode",
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
    error_coefficient: List[IscwsaErrorCoefficient] = field(
        default_factory=list,
        metadata={
            "name": "ErrorCoefficient",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "min_occurs": 1,
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
