from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.extension_name_value import ExtensionNameValue
from witsml20.pressure_measure import PressureMeasure
from witsml20.stim_pressure_flow_rate import StimPressureFlowRate

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class StimStepTest:
    """
    An injection test, plotted pressure against injection rate, where a curve
    deflection and change of slope indicates the fracture breakdown pressure.

    :ivar fracture_extension_pres: The pressure necessary to extend the
        fracture once initiated. The fracture extension pressure may
        rise slightly with increasing fracture length and/or height
        because of friction pressure drop down the length of the
        fracture.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar pres_measurement: A pressure and fluid rate data reading.
    :ivar uid: Unique identifier for this instance of StimStepTest.
    """
    fracture_extension_pres: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "FractureExtensionPres",
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
    pres_measurement: List[StimPressureFlowRate] = field(
        default_factory=list,
        metadata={
            "name": "PresMeasurement",
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
