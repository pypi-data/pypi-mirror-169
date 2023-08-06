from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.error_model_misalignment_mode import ErrorModelMisalignmentMode
from witsml20.length_measure import LengthMeasure
from witsml20.length_per_time_measure import LengthPerTimeMeasure
from witsml20.plane_angle_measure import PlaneAngleMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class IscwsaModelParameters:
    """
    Various parameters controlling the generation of the survey variance.

    :ivar misalignment_mode: Choice of mathmatical modelling of
        misalignment.
    :ivar gyro_initialization: Inclination at which gyro initialization
        occurs.
    :ivar gyro_reinitialization_distance: Maximum length of continuous
        survey before re-initialization.
    :ivar switching: True if the survey tool is rotated at inclinations
        greater than 90 degrees.
    :ivar noise_reduction_factor: Factor applied to random noise error
        terms, depending on the mode of gyro initialization. Values must
        be greater than zero and less than or equal to 1.
    :ivar gyro_running_speed: Speed at which the tool traverses the
        wellbore during a continuous survey.
    """
    misalignment_mode: Optional[ErrorModelMisalignmentMode] = field(
        default=None,
        metadata={
            "name": "MisalignmentMode",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    gyro_initialization: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "GyroInitialization",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    gyro_reinitialization_distance: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "GyroReinitializationDistance",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    switching: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Switching",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    noise_reduction_factor: Optional[float] = field(
        default=None,
        metadata={
            "name": "NoiseReductionFactor",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    gyro_running_speed: Optional[LengthPerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "GyroRunningSpeed",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
