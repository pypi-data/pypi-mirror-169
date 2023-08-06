from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.chromatograph import Chromatograph
from witsml20.data_object_reference import DataObjectReference
from witsml20.drilling_parameters import DrillingParameters
from witsml20.md_interval import MdInterval
from witsml20.mud_gas import MudGas

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class MudlogReportInterval:
    """
    The interval at which the report on the mud log was taken, detailing
    cuttings, interpreted geology, and show evaluation.

    :ivar md_interval: Measured depth interval.
    :ivar cuttings_geology_interval: The cuttings geology interval that
        is part of this mud log report.
    :ivar interpreted_geology_interval: The interpreted geology interval
        that is part of this mud log report.
    :ivar show_evaluation_interval: The show evaluation interval that is
        part of this mud log report.
    :ivar chromatograph:
    :ivar drilling_parameters:
    :ivar mud_gas:
    :ivar uid: Unique identifier for this instance of
        MudLogReportInterval.
    """
    md_interval: Optional[MdInterval] = field(
        default=None,
        metadata={
            "name": "MdInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    cuttings_geology_interval: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "CuttingsGeologyInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    interpreted_geology_interval: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "InterpretedGeologyInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    show_evaluation_interval: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "ShowEvaluationInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    chromatograph: Optional[Chromatograph] = field(
        default=None,
        metadata={
            "name": "Chromatograph",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    drilling_parameters: List[DrillingParameters] = field(
        default_factory=list,
        metadata={
            "name": "DrillingParameters",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    mud_gas: List[MudGas] = field(
        default_factory=list,
        metadata={
            "name": "MudGas",
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
