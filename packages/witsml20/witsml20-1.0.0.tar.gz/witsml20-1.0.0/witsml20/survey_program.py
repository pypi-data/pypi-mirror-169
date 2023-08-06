from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.abstract_object import AbstractObject
from witsml20.data_object_reference import DataObjectReference
from witsml20.survey_section import SurveySection

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class SurveyProgram(AbstractObject):
    """Captures information about the nature, range, and sequence of
    directional surveying tools run in a wellbore for the management of
    positional uncertainty.

    This object is uniquely identified within the context of one
    wellbore object.

    :ivar survey_ver: Survey version number, incremented every time the
        program is modified.
    :ivar engineer: Name of the engineer.
    :ivar final: Is program  final or intermediate/preliminary?
    :ivar survey_section:
    :ivar wellbore:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/witsmlv2"

    survey_ver: Optional[int] = field(
        default=None,
        metadata={
            "name": "SurveyVer",
            "type": "Element",
            "required": True,
            "min_inclusive": 0,
        }
    )
    engineer: Optional[str] = field(
        default=None,
        metadata={
            "name": "Engineer",
            "type": "Element",
            "max_length": 64,
        }
    )
    final: Optional[str] = field(
        default=None,
        metadata={
            "name": "Final",
            "type": "Element",
            "max_length": 64,
        }
    )
    survey_section: List[SurveySection] = field(
        default_factory=list,
        metadata={
            "name": "SurveySection",
            "type": "Element",
        }
    )
    wellbore: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Wellbore",
            "type": "Element",
            "required": True,
        }
    )
