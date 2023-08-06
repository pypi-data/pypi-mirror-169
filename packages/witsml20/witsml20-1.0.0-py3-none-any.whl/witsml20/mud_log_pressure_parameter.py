from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.mud_log_parameter import MudLogParameter
from witsml20.pressure_measure_ext import PressureMeasureExt
from witsml20.pressure_parameter_kind import PressureParameterKind

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class MudLogPressureParameter(MudLogParameter):
    """
    Describes the kind and value of mud log parameters that are expressed in
    units of pressure.

    :ivar value: The value of the parameter in pressure units.
    :ivar pressure_parameter_kind:
    """
    value: Optional[PressureMeasureExt] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    pressure_parameter_kind: Optional[PressureParameterKind] = field(
        default=None,
        metadata={
            "name": "PressureParameterKind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
