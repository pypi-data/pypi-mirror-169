from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.abstract_temperature_pressure import AbstractTemperaturePressure
from witsml20.pressure_measure import PressureMeasure
from witsml20.thermodynamic_temperature_measure import ThermodynamicTemperatureMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class TemperaturePressure(AbstractTemperaturePressure):
    """
    temperature and pressure.

    :ivar temperature: The temperature to which the density has been
        corrected. If given, then a pressure must also be given. Common
        standard temperatures are: 0 degC, 15 degC, 60 degF. If neither
        standardTempPres nor temp,pres are specified then the standard
        condition is defined by standardTempPres at the productVolume
        root.
    :ivar pressure: The pressure to which the density has been
        corrected. If given, then a temperature must also be given.
        Common standard pressures are: 1 atm and 14.696 psi (which are
        equivalent). If neither standardTempPres nor temp,pres are
        specified then the standard condition is defined by
        standardTempPres at the productVolume root.
    """
    temperature: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "Temperature",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    pressure: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "Pressure",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
