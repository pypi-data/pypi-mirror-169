from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.angular_velocity_measure import AngularVelocityMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class RheometerViscosity:
    """
    Viscosity reading of the rheometer.

    :ivar speed: Rotational speed of the rheometer, typically in RPM.
    :ivar viscosity: The raw reading from a rheometer. This could be ,
        but is not necessarily, a viscosity.
    :ivar uid: Unique identifier for this instance of
        RheometerViscosity.
    """
    speed: Optional[AngularVelocityMeasure] = field(
        default=None,
        metadata={
            "name": "Speed",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    viscosity: Optional[float] = field(
        default=None,
        metadata={
            "name": "Viscosity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
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
