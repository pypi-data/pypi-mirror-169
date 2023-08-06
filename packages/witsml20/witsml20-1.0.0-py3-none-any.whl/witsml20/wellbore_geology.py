from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.abstract_object import AbstractObject
from witsml20.cuttings_geology import CuttingsGeology
from witsml20.data_object_reference import DataObjectReference
from witsml20.interpreted_geology import InterpretedGeology
from witsml20.md_interval import MdInterval
from witsml20.show_evaluation import ShowEvaluation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class WellboreGeology(AbstractObject):
    """
    The transferrable class of the WellboreGeology object.

    :ivar md_interval: [maintained by the server] The interval that
        contains the minimum and maximum measured depths for all
        wellbore geology types under this wellbore geology entry.
    :ivar show_interval_set:
    :ivar interpreted_geology_interval_set:
    :ivar wellbore:
    :ivar cuttings_interval_set:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/witsmlv2"

    md_interval: Optional[MdInterval] = field(
        default=None,
        metadata={
            "name": "MdInterval",
            "type": "Element",
            "required": True,
        }
    )
    show_interval_set: Optional[ShowEvaluation] = field(
        default=None,
        metadata={
            "name": "ShowIntervalSet",
            "type": "Element",
        }
    )
    interpreted_geology_interval_set: Optional[InterpretedGeology] = field(
        default=None,
        metadata={
            "name": "InterpretedGeologyIntervalSet",
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
    cuttings_interval_set: Optional[CuttingsGeology] = field(
        default=None,
        metadata={
            "name": "CuttingsIntervalSet",
            "type": "Element",
        }
    )
